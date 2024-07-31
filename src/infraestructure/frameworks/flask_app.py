from flask import Flask
from flask_injector import FlaskInjector
from src.infraestructure.di.container import DI
from src.infraestructure.config.config import Config
from src.adapters.controllers.user_controller import UserController

class App:
  @staticmethod
  def create_app():
    app = Flask(__name__)
    App.register_blueprints(app)
    App.configure_injector(app)
    return app

  @staticmethod
  def configure_injector(app):
    FlaskInjector(app=app, modules=[DI.configure])

  @staticmethod
  def register_blueprints(app):
    app.register_blueprint(UserController.user_bp, url_prefix=f'/api/{Config.API_VERSION}/users')
