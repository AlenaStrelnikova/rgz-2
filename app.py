from flask import Flask
from base import base
from flask_sqlalchemy import SQLAlchemy
from Db import db
from Db.models import Users
from flask_login import LoginManager


app = Flask(__name__)
app.register_blueprint(base)


app.secret_key = '123'
user_db = 'alena_knowledge_base_rgz'
host_ip = '127.0.0.1'
host_port = '5432'
database_name = 'knowledge_base_rgz'
password = '12345'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password}@{host_ip}:{host_port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'base.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(user_id):
    return Users.query.get(int(user_id))

with app.app_context():
    db.create_all()