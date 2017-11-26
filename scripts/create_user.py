#!/usr/bin/env python3
import sys

from weather.app import app
from weather.db import db
from weather.models import User
from weather.security import password_context

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(1)

    with app.app_context():
        user = User()
        user.name = sys.argv[1]
        user.password = password_context.hash(sys.argv[2])
        db.session.add(user)
        db.session.commit()
