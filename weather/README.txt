How to start:

1) Create virtual environment:
    virtualenv your-venv-path -p python3
...and activate it:
    source your-venv-path/bin/activate

2) Setup application:
    pip install .

3) Create database:
    scripts/create_db.py

4) Generate temperature data:
    scripts/generate_data.py

5) Create user:
    scripts/create_user.py username password

6) Run application:
    scripts/run.py

7) Open http://localhost:5000/
