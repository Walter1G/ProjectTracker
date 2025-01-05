from flask import Flask
from .extensions import db, migrate, ma
from .blueprints.projects_bp import project_bp
from .models import *


def create_app():


    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///tmdProject.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)
    migrate.init_app(app,db)
    ma.init_app(app)

    app.register_blueprint(project_bp)


    @app.route("/")
    def home():
        return "Welcome to Project Tracking v1.0"



    return app