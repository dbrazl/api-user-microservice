from flask import Flask
from flask_injector import FlaskInjector
from flask_jwt_extended import JWTManager
from src.infraestructure.di.container import DI
from src.infraestructure.config.config import Config
from src.infraestructure.frameworks.flask_user_routes import FlaskUserRoutes

class App:
  @staticmethod
  def create_app() -> None:
    app = Flask(__name__)
    App.register_blueprints(app)
    App.configure_authorization(app)
    App.configure_injector(app)
    return app

  @staticmethod
  def configure_injector(app: Flask) -> None:
    flask_injector = FlaskInjector(app=app, modules=[DI.configure])
    app.injector = flask_injector.injector

  @staticmethod
  def register_blueprints(app: Flask) -> None:
    app.register_blueprint(FlaskUserRoutes.user_bp, url_prefix=f'/api/{Config.API_VERSION}/users')

  @staticmethod
  def configure_authorization(app: Flask) -> None:
    app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
    JWTManager(app)
