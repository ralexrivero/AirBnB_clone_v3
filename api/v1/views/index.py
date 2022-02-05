#!/usr/bin/python3
'''api status'''
import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import jsonify
from api.v1.views import app_views


@app_views.route('/returnstuff')
def returnstuff():
    '''return stuff'''
    return jsonify({'output' : num_dict})
