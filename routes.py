#!/usr/bin/python3
from flask import Blueprint, render_template, redirect, request, url_for

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

@main_routes.route("/booking", methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Process the booking form data
        return redirect(url_for('confirmation'))
    return render_template('booking.html')

@main_routes.route("/auth")
def get_authentication():
    return render_template("auth.html")

@main_routes.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
