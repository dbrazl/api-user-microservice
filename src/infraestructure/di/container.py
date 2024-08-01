from injector import Binder, singleton
from src.infraestructure.network.http_status import HttpStatus
from src.infraestructure.repositories.sql_alchemy_user_repository import SqlAlchemyUserRepository
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface
from src.application.exceptions.exception_messages import ExceptionMessages
from src.application.interfaces.factories.index_users_factory_interface import IndexUsersFactoryInterface
from src.application.factories.index_users_factory import IndexUsersFactory
from src.application.interfaces.use_cases.index_user_by_id_use_case_interface import IndexUserByIdUseCaseInterface
from src.application.use_cases.index_user_by_id_use_case import IndexUserByIdUseCase

class DI:
  @staticmethod
  def configure(binder: Binder):
    binder.bind(HttpStatusInterface, to=HttpStatus, scope=singleton)
    binder.bind(UserRepositoryInterface, to=SqlAlchemyUserRepository, scope=singleton)
    binder.bind(ExceptionMessagesInterface, to=ExceptionMessages, scope=singleton)
    binder.bind(IndexUsersFactoryInterface, to=IndexUsersFactory, scope=singleton)
    binder.bind(IndexUserByIdUseCaseInterface, to=IndexUserByIdUseCase, scope=singleton)
