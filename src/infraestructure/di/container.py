from injector import Binder, singleton
from src.infraestructure.network.http_status import HttpStatus
from src.infraestructure.repositories.sql_alchemy_user_repository import SqlAlchemyUserRepository
from src.infraestructure.exceptions.exception_messages import ExceptionMessages
from src.adapters.interfaces.controllers.user_controller_interface import UserControllerInterface
from src.adapters.controllers.user_controller import UserController
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface
from src.application.interfaces.factories.index_users_factory_interface import IndexUsersFactoryInterface
from src.application.factories.index_users_factory import IndexUsersFactory
from src.application.interfaces.use_cases.index_user_by_id_use_case_interface import IndexUserByIdUseCaseInterface
from src.application.use_cases.index_user_by_id_use_case import IndexUserByIdUseCase
from src.application.interfaces.use_cases.index_users_use_case_interface import IndexUsersUseCaseInterface
from src.application.use_cases.index_users_use_case import IndexUsersUseCase
from src.application.interfaces.use_cases.index_user_by_email_use_case_interface import IndexUserByEmailUseCaseInterface
from src.application.use_cases.index_user_by_email_use_case import IndexUserByEmailUseCase
from src.application.interfaces.use_cases.index_users_by_name_use_case_interface import IndexUsersByNameUseCaseInterface
from src.application.use_cases.index_users_by_name_use_case import IndexUsersByNameUseCase
from src.application.interfaces.use_cases.store_user_use_case_interface import StoreUserUseCaseInterface
from src.application.use_cases.store_user_use_case import StoreUserUseCase
from src.application.interfaces.use_cases.update_user_use_case_interface import UpdateUserUseCaseInterface
from src.application.use_cases.update_user_use_case import UpdateUserUseCase
from src.application.interfaces.use_cases.delete_user_use_case_interface import DeleteUserUseCaseInterface
from src.application.use_cases.delete_user_use_case import DeleteUserUseCase

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
    binder.bind(IndexUsersByNameUseCaseInterface, to=IndexUsersByNameUseCase, scope=singleton)
    binder.bind(StoreUserUseCaseInterface, to=StoreUserUseCase, scope=singleton)
    binder.bind(UpdateUserUseCaseInterface, to=UpdateUserUseCase, scope=singleton)
    binder.bind(DeleteUserUseCaseInterface, to=DeleteUserUseCase, scope=singleton)
