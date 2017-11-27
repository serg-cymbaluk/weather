#!/usr/bin/env python3
from datetime import date
import json
import unittest

from weather.app import app
from weather.models import User, Temperature
from weather.security import password_context
import weather.views

class WeatherTestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.testing = True
        self.app = app.test_client()
        from weather.db import db
        self.db = db
        with app.app_context():
            db.create_all()

        self.username = 'user'
        self.password = '111'

    def tearDown(self):
        self.db.drop_all()

    def test_redirect_after_login(self):
        self._create_user()
        response = self._login()

        assert response.status_code == 302

    def test_chart_after_login(self):
        self._create_user()
        self._login()

        response = self.app.get('/chart')
        assert response.status_code == 200

    def test_chart_data(self):
        year = 2017
        month = 1

        for day in range(10):
            temperature = Temperature()
            temperature.date = date(year, month, 1 + day)
            temperature.min_value = 0
            temperature.max_value = 1
            self.db.session.add(temperature)
        self.db.session.commit()

        self._create_user()
        self._login()
        response = self.app.get(
            '/api/temperature/{0}/{1}'.format(year, month)
        )

        data = json.loads(response.data.decode('utf-8'))
        assert len(data) == 10
        assert 'date' in data[0]
        assert 'min_value' in data[0]
        assert 'max_value' in data[0]

    def test_chart_data_permission(self):
        response = self.app.get('/api/temperature/{0}/{1}'.format(2017, 1))
        assert response.status_code != 200

    def _create_user(self):
        user = User()
        user.name = self.username
        user.password = password_context.hash(self.password)
        self.db.session.add(user)
        self.db.session.commit()

    def _login(self):
        return self.app.post('login', data={
            'username': self.username,
            'password': self.password,
        })

if __name__ == '__main__':
    unittest.main()
