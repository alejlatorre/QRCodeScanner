from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class QRCodeData(FlaskForm):
    data = StringField(
        label='Data', validators=[DataRequired(), Length(min=2, max=300)]
    )
    submit = SubmitField(label='Extract QRCode')
