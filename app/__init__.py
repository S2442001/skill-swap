from flask import Flask 
from app.extensions import db, migrate, login_manager 
from app.routes import auth, skill 
from app.config import Config

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth.bp, url_prefix="/")
    app.register_blueprint(skill.bp, url_prefix="/")


    return app



