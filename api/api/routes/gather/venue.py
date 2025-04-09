from flask import Blueprint, jsonify
from flasgger import swag_from

from ...service.errors import *
from ...documentation.gather.venue import gather_venue_doc
from ...service.params.geography import Geography as geo
from ...service.gather import Gather

gather_venue_api = Blueprint('gather_venue_api', __name__, url_prefix='/gather/venue')

@gather_venue_api.route('/', methods=['POST'])
@swag_from(gather_venue_doc)
@handle_errors
def searchArea():
    lat, lon = geo.coordinates()
    radius = geo.radius()
    venues = Gather.venues(lat, lon, radius)

    return jsonify({ 
        'status': 'Success',
        'data': venues
    }), 201
