from abc import ABC, abstractmethod
from src.application.dtos.user_dto import UserDto

class IndexUsersUseCaseInterface(ABC):
  @abstractmethod
  def execute(self) -> list[UserDto]:
    pass
