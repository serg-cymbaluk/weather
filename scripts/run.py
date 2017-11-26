#!/usr/bin/env python3
from flask import Flask

from weather.app import app
import weather.views

if __name__ == '__main__':
    app.run(debug=True)
