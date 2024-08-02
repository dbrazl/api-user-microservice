from abc import ABC, abstractmethod
from src.application.dtos.user_dto import UserDto

class IndexUsersByNameUseCaseInterface(ABC):
  @abstractmethod
  def execute(self, name: str) -> list[UserDto]:
    pass
