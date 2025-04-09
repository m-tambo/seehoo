from flask import request
from ..errors.endpoint_errors import error_coordinates, error_radius

class Geography:
    @staticmethod
    def coordinates():
        try:
            latitude = float(request.args['lat'])
            longitude = float(request.args['lon'])
            return (latitude, longitude)
        except (KeyError, ValueError): raise error_coordinates

    @staticmethod
    def radius(): 
        try:
            r = float(request.args.get('radius', 5000))
            if r > 0: return r
            else: raise ValueError
        except (ValueError): raise error_radius
