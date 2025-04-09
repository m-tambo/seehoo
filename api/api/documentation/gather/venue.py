from ..params.geography import *
from ..errors import *
from ...service.errors.endpoint_errors import *

gather_venue_doc={
    'description': 'Gather venues in a given area',
    'responses': {
        '201': {
            'description': 'Successfully gathered and saved venues in the area',
            'examples': {
                'application/json': {
                    "data": [
                            {
                                "address": "4401 Tejon St, Denver, CO 80211, USA",
                                "latitude": 39.7767994,
                                "longitude": -105.01168729999999,
                                "name": "The Monkey Barrel",
                                "type": "restaurant",
                                "website": "http://www.monkeybarrelbar.com/"
                            },
                            {
                                "address": "2721 Larimer St, Denver, CO 80205, USA",
                                "latitude": 39.7599549,
                                "longitude": -104.9838407,
                                "name": "Larimer Lounge",
                                "type": "event_venue",
                                "website": "http://larimerlounge.com/"
                            }
                    ],
                    "status": "success"
                }
            }
        },
        **e_doc(error_coordinates),
        **e_doc(error_radius),
        **e_doc(error_500),
        **error_external
    },
    'tags': ['gather'],
    'parameters': [
        latitude,
        longitude,
        radius
    ]
}
