from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# SQLALCHEMY

SQLALCHEMY_DATABASE_URI=f'''postgresql://{
    environ.get('PG_USER')
}:{
    environ.get('PG_PASSWORD')
}@db:5432/{
    environ.get('PG_DB')
}'''

SQLALCHEMY_TRACK_MODIFICATIONS = False

# SWAGGER

SWAGGER = {
    'title': F'{environ.get("APP_NAME", "seehoo")} API',
    'uiversion': 3,
    'specs': [
        {
            'endpoint': 'apispec_1',
            'route': '/api/docs/apispec_1.json',
            'rule_filter': lambda rule: True,  # all in
            'model_filter': lambda tag: True,  # all in
        }
    ],
    'static_url_path': '/static/swagger',
    'specs_route': environ.get('SWAGGER_URL', '/api/docs/'),
    'headers': [],
}

SWAGGER_URL = environ.get('SWAGGER_URL')
