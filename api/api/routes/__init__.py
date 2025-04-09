from .home import home_api;
from .gather import (
    gather_venue_api,
    gather_show_api
)

def register_routes(app):
    app.register_blueprint(home_api)
    blueprints = [
        gather_venue_api,
        gather_show_api
    ]
    for b in blueprints:
        app.register_blueprint(
            b, url_prefix='/api/v1' + b.url_prefix
        )
