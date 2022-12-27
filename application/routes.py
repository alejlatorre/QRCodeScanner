import os
import secrets
import urllib.request

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from application import app
from src.engine import QRCodeScanner

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template(template_name_or_list='layout.html')


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

        qrcs = QRCodeScanner()
        image = qrcs.read_image(
            filename=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        )
        scanned_filename = filename.split('.')
        scanned_filename = scanned_filename[0] + '_scanned.' + scanned_filename[1]
        qr_text = qrcs.extract_info(
            img=image,
            save_img=True,
            filepath=os.path.join(app.config['UPLOAD_FOLDER'], scanned_filename),
        )
        for text in qr_text:
            flash(message=text)

        files = [filename, scanned_filename]
        return render_template(template_name_or_list='layout.html', files=files)
    else:
        flash(message='Allowed image types are: png, jpg, jpeg')
        return redirect(location=request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(location=url_for('static', filename=filename), code=301)
