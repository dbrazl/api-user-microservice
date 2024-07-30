from flask import Flask
from flask_injector import FlaskInjector
from src.infraestructure.di.container import DI

class App:
  @staticmethod
  def create_app():
    app = Flask(__name__)
    App.configure_injector(app)
    return app

  @staticmethod
  def configure_injector(app):
    FlaskInjector(app=app, modules=[DI.configure])
