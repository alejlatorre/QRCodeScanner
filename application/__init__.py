import os

from flask import Flask

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))

app.config['SECRET_KEY'] = '96c2cfcd56e6532d791efe16d6577965d2a39fdc'
app.config['UPLOAD_FOLDER'] = os.path.join(dir_path, 'static')

from application import routes
