from injector import Binder, singleton
from src.core.interfaces.network.http_status_interface import HttpStatusInterface
from src.infraestructure.network.http_status import HttpStatus

class DI:
  @staticmethod
  def configure(binder: Binder):
    binder.bind(HttpStatusInterface, to=HttpStatus, scope=singleton)
