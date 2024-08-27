from flask import Flask

from main_page import main_page
from music_page import music_page

app = Flask(__name__)

app.register_blueprint(main_page, url_prefix='/')
app.register_blueprint(music_page, url_prefix='/')

app.run(host= '0.0.0.0', port= 9999, debug= True)