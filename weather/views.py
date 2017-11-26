import calendar
from datetime import date

from flask import request, render_template, redirect, jsonify
from flask_login import login_required, login_user, logout_user
from sqlalchemy.sql import func

from weather.app import app
from weather.db import db
from weather.models import User, Temperature
from weather.security import password_context


@app.route('/')
def index():
    return redirect('/chart')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        user = User.query.filter(
            User.name == request.form['username']
        ).one_or_none()
        if user:
            is_valid = password_context.verify(
                request.form['password'],
                user.password
            )
            if is_valid:
                login_user(user)
                return redirect('/chart')
        error = 'Invalid username or password. Please try again.'
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route('/chart')
@login_required
def chart():
    min_date = db.session.query(func.min(Temperature.date)).scalar()
    this_year = date.today().year
    years = range(min_date and min_date.year or this_year, this_year + 1)
    months = [{
        'number': number,
        'name': calendar.month_name[number],
    } for number in range(1, 13)]
    return render_template('chart.html', years=sorted(years), months=months)


@app.route('/api/temperature/<int:year>/<int:month>', methods=['GET'])
@login_required
def get_temperature(year, month):
    unused, last_day_of_month = calendar.monthrange(year, month)
    first_day = date(year, month, 1)
    last_day = date(year, month, last_day_of_month)

    query = Temperature.query.filter(
        Temperature.date.between(first_day, last_day)
    )

    data = [{
        'date': temperature.date.isoformat(),
        'min_value': temperature.min_value,
        'max_value': temperature.max_value,
    } for temperature in query]
    return jsonify(data)
