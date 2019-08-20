import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://toystore:123456@db:5432/toystore'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
