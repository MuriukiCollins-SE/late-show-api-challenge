from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import app_config
from models import db
from controllers.user_controller import user_bp
from controllers.guest_controller import guest_bp
from controllers.episode_controller import episode_bp
from controllers.appearance_controller import appearance_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config['production'])
    
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)
    
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(guest_bp, url_prefix='/api')
    app.register_blueprint(episode_bp, url_prefix='/api')
    app.register_blueprint(appearance_bp, url_prefix='/api')
    
    @app.route('/')
    def home():
        return {"message": "Welcome to the Late Show API"}, 200
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)