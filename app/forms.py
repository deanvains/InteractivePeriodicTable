from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from app.models import periodicTable

class DescForm(FlaskForm):
    newDesc = StringField('')
    submit = SubmitField('Update')
