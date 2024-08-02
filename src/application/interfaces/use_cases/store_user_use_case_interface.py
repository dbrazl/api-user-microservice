from abc import ABC, abstractmethod
from src.application.dtos.user_dto import UserDto

class StoreUserUseCaseInterface(ABC):
  @abstractmethod
  def execute(self, user: UserDto) -> None:
    pass
