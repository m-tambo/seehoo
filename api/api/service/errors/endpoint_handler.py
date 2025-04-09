import requests
from os import environ
from traceback import print_exc
from flask import jsonify

debug_mode = environ.get('FLASK_DEBUG') == '1'

class EndpointError(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
    
    @property
    def response(self):
        return jsonify({
            'status': 'error',
            'message': self.message
        }), self.status_code
    
class ExternalEndpointError(EndpointError):
    def __init__(self, response):
        message = f'<{response.status_code} EXTERNAL> '
        message += f'{response.reason} - {response.text}'
        super().__init__(message, 503)

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except EndpointError as e:
            if debug_mode: print_exc()
            return e.response
        except requests.exceptions.HTTPError as e:
            if debug_mode: print_exc()
            return ExternalEndpointError(e.response).response
        except Exception as e:
            if debug_mode: print_exc()
            return jsonify({
                'status': 'error',
                'message': 'Something unexpected went wrong: ' + str(e)
            }), 500
    return wrapper
