from ast import Str
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length

class UserSignUpForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class LoginForm(FlaskForm):
    """Form for logging in users."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class UserEditForm(FlaskForm):
    """Form for editting users."""

    username = StringField('Enter new username', validators=[])
    password = PasswordField('Enter new password', validators=[])
    confirmpass = PasswordField('Confirm Password', validators=[Length(min=6)])