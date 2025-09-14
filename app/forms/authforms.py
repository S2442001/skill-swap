from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, EmailField, SubmitField 
from wtforms.validators import DataRequired, Length 

class RegisterForm(FlaskForm):
    username=StringField("username", validators=[DataRequired(), Length(min=3, max=20)])
    email=EmailField("email", validators=[DataRequired()])
    password=StringField("password", validators=[DataRequired(), Length(min=8, max=16)])
    submit=SubmitField("Register") 

class LoginForm(FlaskForm):
    username=StringField("username", validators=[DataRequired()])
    password=StringField("password",validators=[DataRequired()])
    submit=SubmitField("Login")