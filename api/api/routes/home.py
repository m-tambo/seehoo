from os import environ
from flask import Blueprint, redirect, jsonify
from flasgger import swag_from

home_api = Blueprint('api', __name__)

@home_api.route('/')
@swag_from('../documentation/home.yml')
def welcome():
    return redirect(environ.get('SWAGGER_URL'), code=302)
