from injector import inject
from src.application.interfaces.factories.index_users_factory_interface import IndexUsersFactoryInterface
from src.application.interfaces.use_cases.index_user_by_id_use_case_interface import IndexUserByIdUseCaseInterface
from src.application.interfaces.use_cases.index_user_by_email_use_case_interface import IndexUserByEmailUseCaseInterface
from src.application.interfaces.use_cases.index_users_use_case_interface import IndexUsersUseCaseInterface

class IndexUsersFactory(IndexUsersFactoryInterface):
  @inject
  def __init__(
    self,
    index_user_by_id_use_case: IndexUserByIdUseCaseInterface,
    index_user_by_email_use_case: IndexUserByEmailUseCaseInterface,
    index_users_use_case: IndexUsersUseCaseInterface,
  ) -> None:
    self.index_user_by_id_use_case = index_user_by_id_use_case
    self.index_user_by_email_use_case = index_user_by_email_use_case
    self.index_users_use_case = index_users_use_case

  def make_index_use_case(self, filter: str) -> IndexUserByIdUseCaseInterface | IndexUserByEmailUseCaseInterface | IndexUsersUseCaseInterface:
    match filter:
      case 'id':
        return self.index_user_by_id_use_case

      case 'email':
        return self.index_user_by_email_use_case

      case _:
        return self.index_users_use_case
