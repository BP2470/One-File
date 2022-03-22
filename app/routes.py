from app import myobj
from flask import render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

name = 'Lisa'
city_names = ['Paris','London','Rome','Tahiti']

class LoginForm(FlaskForm):
    username = StringField('City Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')
    
@myobj.route('/', methods =['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f'{form.username.data}')
    return render_template('home.html', name=name,city_names=city_names,form=form)