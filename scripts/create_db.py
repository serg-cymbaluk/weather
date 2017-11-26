#!/usr/bin/env python3
from weather.db import db
import weather.models

if __name__ == '__main__':
    db.create_all()
