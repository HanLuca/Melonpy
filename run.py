from flask import Flask
import random

#! src files module
from src import home

app = Flask(__name__)

app.register_blueprint(home.page_home)

app.config['SECRET_KEY'] = random.randrange(1111, 9999)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 9999, debug= True)