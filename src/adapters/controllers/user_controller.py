from injector import inject
from src.adapters.interfaces.controllers.user_controller_interface import UserControllerInterface
from src.application.interfaces.factories.index_users_factory_interface import IndexUsersFactoryInterface
from src.application.dtos.user_dto import UserDto

class UserController(UserControllerInterface):
  @inject
  def __init__(self, index_users_factory: IndexUsersFactoryInterface) -> None:
    self.index_users_factory = index_users_factory

  def health(self) -> None:
    return ''

  def index(self, filter: str, filter_value: str) -> list[UserDto] | UserDto:
    index_use_case = self.index_users_factory.make_index_use_case(filter)
    user_dto_or_list = index_use_case.execute(filter_value) if filter else index_use_case.execute()
    return user_dto_or_list
