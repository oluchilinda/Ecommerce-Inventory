

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():

    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'dev.sqlite')


class TestingConfig(Config):

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'test.sqlite')


class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'prod.sqlite')


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
