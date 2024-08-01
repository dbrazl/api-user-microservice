from injector import Binder, singleton
from src.infraestructure.network.http_status import HttpStatus
from src.infraestructure.repositories.sql_alchemy_user_repository import SqlAlchemyUserRepository
from src.adapters.interfaces.controllers.user_controller_interface import UserControllerInterface
from src.adapters.controllers.user_controller import UserController
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface
from src.application.exceptions.exception_messages import ExceptionMessages
from src.application.interfaces.factories.index_users_factory_interface import IndexUsersFactoryInterface
from src.application.factories.index_users_factory import IndexUsersFactory
from src.application.interfaces.use_cases.index_user_by_id_use_case_interface import IndexUserByIdUseCaseInterface
from src.application.use_cases.index_user_by_id_use_case import IndexUserByIdUseCase
from src.application.interfaces.use_cases.index_users_use_case_interface import IndexUsersUseCaseInterface
from src.application.use_cases.index_users_use_case import IndexUsersUseCase
from src.application.interfaces.use_cases.index_user_by_email_use_case_interface import IndexUserByEmailUseCaseInterface
from src.application.use_cases.index_user_by_email_use_case import IndexUserByEmailUseCase

class DI:
  @staticmethod
  def configure(binder: Binder) -> None:
    binder.bind(HttpStatusInterface, to=HttpStatus, scope=singleton)
    binder.bind(UserControllerInterface, to=UserController, scope=singleton)
    binder.bind(UserRepositoryInterface, to=SqlAlchemyUserRepository, scope=singleton)
    binder.bind(ExceptionMessagesInterface, to=ExceptionMessages, scope=singleton)
    binder.bind(IndexUsersFactoryInterface, to=IndexUsersFactory, scope=singleton)
    binder.bind(IndexUserByIdUseCaseInterface, to=IndexUserByIdUseCase, scope=singleton)
    binder.bind(IndexUsersUseCaseInterface, to=IndexUsersUseCase, scope=singleton)
    binder.bind(IndexUserByEmailUseCaseInterface, to=IndexUserByEmailUseCase, scope=singleton)
