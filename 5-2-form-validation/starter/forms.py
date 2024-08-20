from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MyForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Submit')
