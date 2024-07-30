import os
from src.core.interfaces.config_interface import ConfigInterface

class Config(ConfigInterface):
  PORT = os.getenv('PORT')
  ENVIRONMENT = os.getenv('ENVIRONMENT')
  VERSION = os.getenv('API_VERSION')
