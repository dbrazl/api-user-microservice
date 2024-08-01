from injector import inject
from src.application.interfaces.factories.index_users_factory_interface import IndexUsersFactoryInterface
from src.application.interfaces.use_cases.index_user_by_id_use_case_interface import IndexUserByIdUseCaseInterface
from src.application.interfaces.use_cases.index_users_use_case_interface import IndexUsersUseCaseInterface

class IndexUsersFactory(IndexUsersFactoryInterface):
  @inject
  def make_index(
    self,
    filter: str,
    index_user_by_id: IndexUserByIdUseCaseInterface,
    index_users: IndexUsersUseCaseInterface
  ) -> IndexUserByIdUseCaseInterface | IndexUsersUseCaseInterface:
    match filter:
      case 'id':
        return index_user_by_id

      case _:
        return index_users
