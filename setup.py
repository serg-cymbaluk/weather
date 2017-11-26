from setuptools import setup, find_packages

setup(
    name='weather',
    version='0.1.0',
    packages=find_packages(),
    package_data={
        'weather': [
            'static/css/*.css',
            'static/js/*.js',
            'templates/*.html',
        ]
    },
    install_requires=[
        'Flask',
        'Flask-Login',
        'Flask-SQLAlchemy',
        'passlib',
        'SQLAlchemy',
    ]
)
