from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.secret_key = 'f2073051-0c3d-4ed2-b3c9-7ff1e68b396d'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
