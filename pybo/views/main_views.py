from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('message.list_msg'))

@bp.route('/hello')
def hello_pybo():
    return 'Hello Pybo!'
