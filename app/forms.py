from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, IntegerField
from app.models import periodicTable

class DescForm(FlaskForm):
    newDesc = StringField('')
    submit = SubmitField('Update')

class newElement(FlaskForm):
    eid = IntegerField()
    ename = StringField()
    submit = SubmitField('input')