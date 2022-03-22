from flask import Flask
myobj = Flask(__name__)
myobj.secret_key = 'you-will-never-guess'
from app import routes