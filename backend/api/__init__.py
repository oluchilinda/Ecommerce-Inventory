########################
###### app setup #######
########################

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config
from flask_jwt_extended import JWTManager
# from flask_marshmallow import Marshmallow


db = SQLAlchemy()


def create_app(config_name):
    from .models import Category, Product

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    Migrate(app, db)
    jwt = JWTManager(app)

    from .products_views import main as product_blueprint
    app.register_blueprint(product_blueprint)

    return app
