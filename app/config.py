from os.path import abspath, join, dirname

BASE_DIR = abspath(dirname(__file__))

class Config:
    SECRET_KEY = '31231231j3n1iifn1onong14nf41onfn31fu9n1vjo1niu1n3rn'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{join(BASE_DIR, 'site.db')}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False