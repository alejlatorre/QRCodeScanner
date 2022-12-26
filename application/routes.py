import secrets

from flask import render_template, request

from application import app
from application.forms import QRCodeData
from src.engine import QRCodeScanner


@app.route('/')
def index():
    return render_template(template_name_or_list='layout.html', title='Home Page')


@app.route('/extract_qrcode', methods=['POST', 'GET'])
def index_page():
    form = QRCodeData()

    if request.method == 'POST':
        if form.validate_on_submit():
            data = form.data.data
            image_name = f'{secrets.token_hex(10)}.png'
            qrcode_location = f'{app.config["UPLOAD_PATH"]}/{image_name}'

            try:
                qrcs = QRCodeData()
                image = qrcs.read_image(qrcode_location)
                qr_text = qrcs.extract_info(img=image)
            except Exception as ex:
                print(ex)
            except ValueError as ve:
                print(ve)

            return render_template(
                template_name_or_list='extracted_qrcode.html',
                title='Extracted',
                image=image_name,
            )
    else:
        return render_template(
            template_name_or_list='extract_qrcode.html', title='Index Page', form=form
        )
