#!/usr/bin/python3
from flask import Blueprint, render_template

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/')
@main_routes.route('/home')
def get_index():
    return render_template('index.html')


@main_routes.route('/about')
def show_about():
    return render_template('a_about.html')

@main_routes.route("/services")
def show_services():
    return render_template("services.html")

@main_routes.route("/booking")
def book_services():
    return render_template("booking.html")

@main_routes.route("/auth")
def get_authentication():
    return render_template("auth.html")
