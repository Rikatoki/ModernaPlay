from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)
    return app