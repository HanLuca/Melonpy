from flask import Blueprint

page_home = Blueprint('pageHome', __name__, url_prefix= '/home')

@page_home.route('/')
def pageHome__Home():
    return 'dd'