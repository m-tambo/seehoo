radius = {
    'name': 'radius',
    'in': 'query',
    "type": "string",
    "description": "The radius in meters within which to search for venues.",
    "required": False,
    "default": '5000',
    "example": '5000'
}

latitude = {
    'name': 'lat',
    'in': 'query',
    'required': True,
    'schema': {
        'type': 'string',
        'description': 'Latitude of the location'
    }
}

longitude = {
    'name': 'lon',
    'in': 'query',
    'required': True,
    'schema': {
        'type': 'string',
        'description': 'Longitude of the location'
    }
}
