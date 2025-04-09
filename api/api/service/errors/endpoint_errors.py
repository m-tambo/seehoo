from .endpoint_handler import EndpointError, ExternalEndpointError

error_500 = EndpointError(
    'Something unexpected went wrong',
    500
)
{
    'description': 'Error',
    'examples': {
        'application/json': {
            "status": "error",
            "message": 'Something unexpected went wrong: <error message>'
        }
    }
}

error_coordinates = EndpointError(
    'Missing latitude or longitude',
    400
)

error_radius = EndpointError(
    'Radius must be a positive number',
    400
)
