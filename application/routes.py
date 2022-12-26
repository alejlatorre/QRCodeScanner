import os
import secrets
import urllib.request

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from application import app
from application.forms import QRCodeData
from src.engine import QRCodeScanner

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template(template_name_or_list='layout.html', title='Home Page')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash(message='No file part')
        return redirect(location=request.url)
    file = request.files['file']
    if file.filename == '':
        flash(message='No image selected for uploading')
        return redirect(location=request.url)
    if file and allowed_file(filename=file.filename):
        filename = secure_filename(filename=file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash(message='Image successfully uploaded and displayed below')
        return render_template(template_name_or_list='layout.html', filename=filename)
    else:
        flash(message='Allowed image types are: png, jpg, jpeg')
        return redirect(location=request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(location=url_for('static', filename=filename), code=301)


# @app.route('/extract_qrcode', methods=['POST', 'GET'])
# def index_page():
#     form = QRCodeData()

#     if request.method == 'POST':
#         if form.validate_on_submit():
#             data = form.data.data
#             image_name = f'{secrets.token_hex(10)}.png'
#             qrcode_location = f'{app.config["UPLOAD_PATH"]}/{image_name}'

#             try:
#                 qrcs = QRCodeData()
#                 image = qrcs.read_image(qrcode_location)
#                 qr_text = qrcs.extract_info(img=image)
#             except Exception as ex:
#                 print(ex)
#             except ValueError as ve:
#                 print(ve)

#             return render_template(
#                 template_name_or_list='extracted_qrcode.html',
#                 title='Extracted',
#                 image=image_name,
#             )
#     else:
#         return render_template(
#             template_name_or_list='extract_qrcode.html', title='Index Page', form=form
#         )
