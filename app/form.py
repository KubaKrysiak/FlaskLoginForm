from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    login = StringField('Pass your login', validators = [DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Login')