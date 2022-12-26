from flask import render_template

from application import app


@app.route('/index')
def index():
    return render_template(template_name_or_list='layout.html', title='Home Page')
