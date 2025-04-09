import json
import requests
from os import environ

class Google:
    @staticmethod
    def place_api_key(): return environ.get('GOOGLE_PLACES_API_KEY')

    @staticmethod
    def fields(fields):
        result = []
        for f in fields:
            result.append('places.' + f)
        return ','.join(result)
    
    @staticmethod
    def generate_headers(key, params = {}):
        return {
            'Content-Type': 'application/json', 
            'X-Goog-Api-Key': key,
            **params
        }
    
    @staticmethod
    def search_places(lat, lon, radius):
        headers = Google.generate_headers(
                Google.place_api_key(), {
                    'X-Goog-FieldMask': Google.fields([
                        'websiteUri', 
                        'displayName', 
                        'primaryType', 
                        'formattedAddress', 
                        'location'
                    ]),
            })
        data = json.dumps({
            "textQuery": "live music",
            "locationBias": {
                "circle": {
                    "center": {
                        "latitude": lat,
                        "longitude": lon
                    },
                    "radius": radius
                }
            },
        })
        return requests.post(
            url = 'https://places.googleapis.com/v1/places:searchText',
            headers=headers, 
            data=data
        )
        