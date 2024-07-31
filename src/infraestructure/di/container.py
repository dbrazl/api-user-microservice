from injector import Binder, singleton
from src.infraestructure.network.http_status import HttpStatus
from src.infraestructure.repositories.sql_alchemy_user_repository import SqlAlchemyUserRepository
from src.adapters.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.interfaces.use_cases.index_one_user_use_case_interface import IndexOneUserUseCaseInterface
from src.application.use_cases.index_one_user_use_case import IndexOneUserUseCase

class DI:
  @staticmethod
  def configure(binder: Binder):
    binder.bind(HttpStatusInterface, to=HttpStatus, scope=singleton)
    binder.bind(UserRepositoryInterface, to=SqlAlchemyUserRepository, scope=singleton)
    binder.bind(IndexOneUserUseCaseInterface, to=IndexOneUserUseCase, scope=singleton)
