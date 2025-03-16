from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, DateField

class HealthDataForm(FlaskForm):
  date = DateField('Date', format="%Y-%m-%d")
  exercise = IntegerField('Exercise (minutes)')
  meditation = IntegerField("Meditation (minutes)")
  sleep = IntegerField("Sleep (hours)")
  submit = SubmitField("Submit")