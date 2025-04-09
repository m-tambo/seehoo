from os import environ
from flask import Flask
from flasgger import Swagger
from flask_migrate import Migrate

from .api.routes import register_routes
from .api.model.database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py') 
    with app.app_context(): 
        db = init_db(app)
    Migrate(app, db)
    Swagger(
        app, 
        config=app.config.get('SWAGGER'), 
        template_file=None,
    )
    register_routes(app)

    return app

app = create_app()
