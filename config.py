import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://hmjfjnweqgossq:5a21ea9625464f5f0036ee171d6b1afc14f09390656e8437f2dc78869e9052b5@ec2-54-83-201-84.compute-1.amazonaws.com:5432/dd75fobu0b7ecr'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

class DevelopmentConfig(Config):
    FLASK_DEBUG=1