from abc import ABC, abstractmethod
from src.application.interfaces.use_cases.index_user_by_id_use_case_interface import IndexUserByIdUseCaseInterface
from src.application.interfaces.use_cases.index_users_use_case_interface import IndexUsersUseCaseInterface

class IndexUsersFactoryInterface(ABC):
  @abstractmethod
  def make_index(self, filter: str) -> IndexUserByIdUseCaseInterface | IndexUsersUseCaseInterface:
    pass
