#!/usr/bin/python3
from flask import Blueprint

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/')
def index():
    return 'Hello, World!'


@main_routes.route('/about')
def about():
    return 'About page'
