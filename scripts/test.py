#!/usr/bin/env python3
import unittest

from weather.app import app
from weather.models import User
from weather.security import password_context
import weather.views

class WeatherTestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            from weather.db import db
            db.create_all()

        self.username = 'user'
        self.password = '111'

    def tearDown(self):
        from weather.db import db
        db.drop_all()

    def test_redirect_after_login(self):
        self._create_user()
        response = self._login()

        assert response.status_code == 302

    def test_chart_after_login(self):
        self._create_user()
        self._login()

        response = self.app.get('/chart')
        assert response.status_code == 200

    def _create_user(self):
        from weather.db import db
        user = User()
        user.name = self.username
        user.password = password_context.hash(self.password)
        db.session.add(user)
        db.session.commit()

    def _login(self):
        return self.app.post('login', data={
            'username': self.username,
            'password': self.password,
        })

if __name__ == '__main__':
    unittest.main()
