from injector import Binder, singleton
from src.core.interfaces.config_interface import ConfigInterface
from src.infraestructure.config.config import Config

class DI:
  @staticmethod
  def configure(binder: Binder):
    binder.bind(ConfigInterface, to=Config, scope=singleton)
