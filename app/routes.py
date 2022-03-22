from app import myobj
from app.login import LoginForm
from flask import render_template, flash

name = 'Lisa'
city_names = ['Paris','London','Rome','Tahiti']

@myobj.route('/', methods =['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f'{form.username.data}')
    return render_template('home.html', name=name,city_names=city_names,form=form)