from flask import Flask
from flask_session import Session
from datetime import timedelta
import random

from main_page import main_page
from music_page import music_page

from config import token

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=3)
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

app.secret_key = token

app.register_blueprint(main_page, url_prefix='/')
app.register_blueprint(music_page, url_prefix='/')

app.run(host= '0.0.0.0', port= 9999, debug=True)