#!/usr/bin/python3
''' new view for State objects'''

from flask import Flask


@app_views.route('/status', methods=['GET'] strict_slashes=False)
"""GET /api/v1/states"""


def toGet():
    '''getting thing'''
    objects = storage.all('State')
    lista = []
    for state in objects.values():
        lista.append(state.to_dict())
    return jsonify(lista)

@app_views.route('/states/<_id>', methods=['GET'],
                 strict_slashes=False)
"""GET /api/v1/states/<state_id>"""


def toGetid():
    '''Updates a State object id'''
    objects = .get('State', 'state_id')
    if objects is None:
        abort(404)
    return jsonify(objects.to_dict()), 'OK'


'''
DELETE /api/v1/states/<state_id>

POST /api/v1/states

request.get_json

PUT /api/v1/states/<state_id>
'''
