from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class LocationForm(FlaskForm):
    locationFrom = StringField('From', validators=[DataRequired()])
    locationTo = StringField('To', validators=[DataRequired()])
    submit = SubmitField('Search')
