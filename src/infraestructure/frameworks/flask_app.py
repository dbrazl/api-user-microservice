from flask import Flask

class App:
  @staticmethod
  def create_app():
    app = Flask(__name__)
    return app
