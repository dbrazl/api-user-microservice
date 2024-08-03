from injector import inject
from src.adapters.interfaces.controllers.user_controller_interface import UserControllerInterface
from src.application.interfaces.factories.index_users_factory_interface import IndexUsersFactoryInterface
from src.application.interfaces.use_cases.store_user_use_case_interface import StoreUserUseCaseInterface
from src.application.interfaces.use_cases.update_user_use_case_interface import UpdateUserUseCaseInterface
from src.application.interfaces.use_cases.delete_user_use_case_interface import DeleteUserUseCaseInterface
from src.application.dtos.user_dto import UserDto

class UserController(UserControllerInterface):
  @inject
  def __init__(
    self,
    index_users_factory: IndexUsersFactoryInterface,
    store_user_use_case: StoreUserUseCaseInterface,
    update_user_use_case: UpdateUserUseCaseInterface,
    delete_user_use_case: DeleteUserUseCaseInterface
  ) -> None:
    self.index_users_factory = index_users_factory
    self.store_user_use_case = store_user_use_case
    self.update_user_use_case = update_user_use_case
    self.delete_user_use_case = delete_user_use_case

  def health(self) -> None:
    return ''

  def index(self, filter: str, filter_value: str) -> list[UserDto] | UserDto:
    index_use_case = self.index_users_factory.make_index_use_case(filter)
    user_dto_or_list = index_use_case.execute(filter_value) if filter else index_use_case.execute()
    return user_dto_or_list

  def store(self, user: UserDto) -> None:
    self.store_user_use_case.execute(user)

  def update(self, user: UserDto) -> None:
    self.update_user_use_case.execute(user)

  def delete(self, user_id: str) -> None:
    self.delete_user_use_case.execute(user_id)
