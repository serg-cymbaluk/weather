#!/usr/bin/env python3
from datetime import date, timedelta
import random

from weather.db import db
from weather.models import Temperature

average_temperature = [-4, -3, 2, 9, 15, 18, 20, 20, 14, 8, 2, -2]

if __name__ == '__main__':
    today = date.today()
    Temperature.query.delete()
    previous_value = None
    for days in range(1000):
        temperature = Temperature()
        temperature.date = today - timedelta(days=days)
        avg = average_temperature[temperature.date.month - 1]
        max_value = random.randint(avg - 1, avg + 7)
        if not previous_value is None:
            max_value = random.randint(*sorted([max_value, previous_value]))
        temperature.min_value = max_value - random.randint(3, 9)
        temperature.max_value = max_value
        db.session.add(temperature)
    db.session.commit()
