from src.infraestructure.frameworks.flask_app import App

class Server:
  app = App.create_app()

  def listen(self, port, env):
    self.app.run(port=port, debug={True if env == 'DEVELOPER' else False})
