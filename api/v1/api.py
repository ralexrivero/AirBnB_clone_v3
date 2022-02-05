#!/usr/bin/python3
'''Flask server (variable app)'''

from flask import Flask
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from os import getenv

app = Flask(__name__)
admin = Blueprint('admin', __name__, template_folder='templates')

 


@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')
@app.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify_error(ex)
    else:
        return ex