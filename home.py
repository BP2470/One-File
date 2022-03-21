from flask import Flask
from flask import render_template

myobj = Flask(__name__)
name = 'Lisa'
city_names = ['Paris','London','Rome','Tahiti']
'''
        <ul>
            {% for city in city_names}
            <li>{{city}}</li>
            {% endfor %}
        </ul>
'''
#Links need https
@myobj.route('/')
def home():
    return f'''
    <html>
    <head>
    <title>Home page</title>
    <body>
        <h1> Welcome {name}
        <div>
        <a href="https://www.google.com"> not google </a>
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
