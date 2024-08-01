from flask import Flask
from flask_injector import FlaskInjector
from src.infraestructure.di.container import DI
from src.infraestructure.config.config import Config
from src.infraestructure.frameworks.flask_user_routes import FlaskUserRoutes

class App:
  @staticmethod
  def create_app():
    app = Flask(__name__)
    App.register_blueprints(app)
    App.configure_injector(app)
    return app

  @staticmethod
  def configure_injector(app):
    flask_injector = FlaskInjector(app=app, modules=[DI.configure])
    app.injector = flask_injector.injector

  @staticmethod
  def register_blueprints(app):
    app.register_blueprint(FlaskUserRoutes.user_bp, url_prefix=f'/api/{Config.API_VERSION}/users')
