from flask import Flask, render_template, request, jsonify, send_file, after_this_request
import os
import re
import uuid
from werkzeug.utils import secure_filename
from extractor import extract_data
from mapper import map_to_excel_fields
from excel_engine import fill_workbook
import traceback

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024  # 64MB total request limit
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB per individual file
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

_INVALID_SHEET_CHARS = re.compile(r'[\\/?*\[\]:]')

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def _sanitize_sheet_name(name):
    """Replace characters that Excel forbids in sheet names."""
    return _INVALID_SHEET_CHARS.sub('_', name)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/process', methods=['POST'])
def process_image():
    saved_files = []
    try:
        files = request.files.getlist('images')
        if not files or all(f.filename == '' for f in files):
            return jsonify({'error': 'No image files provided'}), 400

        batches = []
        all_results = []

        for file in files:
            if file.filename == '':
                continue
            if not allowed_file(file.filename):
                return jsonify({'error': f'Invalid file type: {file.filename}'}), 400

            # Per-file size check
            file.seek(0, 2)
            file_size = file.tell()
            file.seek(0)
            if file_size > MAX_FILE_SIZE:
                mb = file_size // (1024 * 1024)
                return jsonify({'error': f'File too large: {file.filename} ({mb} MB). Max 10 MB per file.'}), 400

            safe_name = secure_filename(file.filename)
            if not safe_name:
                return jsonify({'error': f'Invalid filename: {file.filename!r}'}), 400

            # Unique prefix prevents collision when multiple files share a name
            filename = f"{uuid.uuid4().hex[:8]}_{safe_name}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            saved_files.append(filepath)

            print(f"Processing {file.filename}...")
            part_json, part_type = extract_data(filepath)
            print(f"  Detected: {part_type}")

            mapped_data = map_to_excel_fields(part_json, part_type)
            label = _sanitize_sheet_name(os.path.splitext(file.filename)[0])
            batches.append((mapped_data, part_type, label))
            all_results.append({
                'filename': file.filename,
                'part_type': part_type,
                'rows': len(mapped_data),
                'data': mapped_data,
            })

        if not batches:
            return jsonify({'error': 'No valid images to process'}), 400

        template_path = "templates/HS_S3DParts.xlsx"
        output_filename = f"Output_SmartParts_{uuid.uuid4().hex[:8]}.xlsx"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        print("Writing Excel...")
        fill_workbook(template_path, output_path, batches)

        combined_data = [row for mapped_data, *_ in batches for row in mapped_data]

        return jsonify({
            'success': True,
            'message': f'Processed {len(batches)} image(s) successfully',
            'output_file': output_filename,
            'images': all_results,
            'extracted_data': combined_data,
        })

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': f'Processing error: {str(e)}'}), 500
    finally:
        for fp in saved_files:
            try:
                os.remove(fp)
            except OSError:
                pass


@app.route('/api/download/<filename>')
def download_file(filename):
    try:
        upload_dir = os.path.realpath(app.config['UPLOAD_FOLDER'])
        filepath = os.path.realpath(os.path.join(upload_dir, secure_filename(filename)))
        if not filepath.startswith(upload_dir + os.sep) and filepath != upload_dir:
            return jsonify({'error': 'Invalid file path'}), 400
        if not os.path.exists(filepath):
            return jsonify({'error': 'File not found'}), 404

        @after_this_request
        def remove_output(response):
            try:
                os.remove(filepath)
            except OSError:
                pass
            return response

        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=os.getenv("FLASK_DEBUG", "0") == "1", port=5000)
