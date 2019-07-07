from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    passwd=PasswordField("Password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('passwd')])
    submit=SubmitField("Sign In")


class LoginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    passwd=PasswordField("Password",validators=[DataRequired()])
    rember=BooleanField("Remember Me")
    submit=SubmitField("Login")