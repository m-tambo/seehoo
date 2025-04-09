from flask import Blueprint, jsonify
from flasgger import swag_from
from datetime import datetime

from ...service.errors import handle_errors
from ...schema.Venue import Venue
from ...service.gather import Gather

gather_show_api = Blueprint('gather_show_api', __name__, url_prefix='/gather/show')

@gather_show_api.route('/', methods=['POST'])
@swag_from({ 
    'tags':['gather'],
    'responses': {
        '200': { 
            'description': 'Success', 
            'examples': { 
                'application/json': { 
                    'status': 'Success', 
                    'data': { 'message': 'Button or link found' }
                } 
            } 
        } 
    }
})
@handle_errors
def searchArea():
    venue = Venue.query.get(12)
    response = Gather.show(venue, date=datetime(2025, 4, 10))
    return jsonify({
        'status': 'Success',
        'data': response
    }), 200
