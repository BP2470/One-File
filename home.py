from flask import Flask
from flask import render_template

myobj = Flask(__name__)
name = 'Lisa'
city_names = ['Paris','London','Rome','Tahiti']

#Links need https
@myobj.route('/')
def home():
    name = 'Lisa'
    city_names = ['Paris','London','Rome','Tahiti']
    return f'''
    <html>
    <head>
    <title>Home page</title>
    <body>
        <h1>Welcome,{name}!</h1>
        <div>
        <a href="www.google.com">notgoogle</a>
        </div>
        <ul>
            <li>{city_names[0]}</li>
            <li>{city_names[1]}</li>
            <li>{city_names[2]}</li>
            <li>{city_names[3]}</li>
        </ul>
    </body>
    </html>
    '''

#myobj.run()
