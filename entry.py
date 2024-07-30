from dotenv import load_dotenv
load_dotenv()

from src.infraestructure.server.server import Server
from src.infraestructure.config.config import Config

if __name__ == '__main__':
  Server().listen(port=Config.PORT, env=Config.ENVIRONMENT)
