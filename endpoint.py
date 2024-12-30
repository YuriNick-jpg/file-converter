from flask import Flask, request, send_file
import os
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader, PdfWriter

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
CONVERTED_FOLDER = 'converted/'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)


@app.route('/convert', methods=['POST'])
def convert_file():
    try:
        file = request.files['file']
        file_format = request.form.get('file_format')
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_path = os.path.join(CONVERTED_FOLDER, filename.split('.')[
                                   0] + '_converted.docx')

        file.save(input_path)

        if file_format == 'pdf_to_docx':
            # Simulação de conversão
            # Aqui você chamaria uma biblioteca específica para PDF para DOCX
            with open(output_path, 'w') as f:
                f.write("Arquivo convertido!")

        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return {"error": str(e)}, 400


if __name__ == '__main__':
    app.run(debug=True)
