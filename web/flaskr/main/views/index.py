from flask import render_template, make_response
from .. import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return make_response(render_template('index.html'))
