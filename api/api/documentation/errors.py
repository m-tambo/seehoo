def e_doc(error):
    code = error.status_code.__str__()
    return { 
        code: {
            'description': error.message,
            'examples': {
                'application/json': {
                    "status": "error",
                    "message": error.message
                }
            }
        }
    }

error_external = {
    '503': {
        'description': 'An external endpoint responded with an error',
        'examples': {
            'application/json': {
                "status": "error",
                "message": '<404 EXTERNAL> Google got deleted'
            }
        }
    }
}
