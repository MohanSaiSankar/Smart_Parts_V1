from flask import Flask, render_template, request, jsonify, send_file
import os
from werkzeug.utils import secure_filename
from extractor import extract_data
from mapper import map_to_excel_fields
from excel_engine import fill_workbook
import traceback

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024  # 64MB for multiple images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

        batches = []        # [(mapped_data, part_type, label), ...]
        all_results = []    # per-image summary for the UI

        for file in files:
            if file.filename == '':
                continue
            if not allowed_file(file.filename):
                return jsonify({'error': f'Invalid file type: {file.filename}'}), 400

            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            saved_files.append(filepath)

            print(f"Processing {filename}...")
            part_json, part_type = extract_data(filepath)
            print(f"  Detected: {part_type}")

            mapped_data = map_to_excel_fields(part_json, part_type)
            label = os.path.splitext(file.filename)[0]  # filename stem as sheet name
            batches.append((mapped_data, part_type, label))
            all_results.append({
                'filename': file.filename,
                'part_type': part_type,
                'rows': len(mapped_data),
                'data': mapped_data,
            })

        if not batches:
            return jsonify({'error': 'No valid images to process'}), 400

        template_path = "templates/Input_Parts.xlsx"
        output_filename = "Output_SmartParts.xlsx"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        print("Writing Excel...")
        fill_workbook(template_path, output_path, batches)

        # Combine all mapped rows for the UI table
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
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        if not os.path.exists(filepath):
            return jsonify({'error': 'File not found'}), 404
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
