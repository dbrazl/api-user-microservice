from injector import Binder, singleton
from src.infraestructure.interfaces.network.http_status_interface import HttpStatusInterface
from src.infraestructure.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.infraestructure.network.http_status import HttpStatus
from src.infraestructure.repositories.sql_alchemy_user_repository import SqlAlchemyUserRepository

class DI:
  @staticmethod
  def configure(binder: Binder):
    binder.bind(HttpStatusInterface, to=HttpStatus, scope=singleton)
    binder.bind(UserRepositoryInterface, to=SqlAlchemyUserRepository, scope=singleton)
