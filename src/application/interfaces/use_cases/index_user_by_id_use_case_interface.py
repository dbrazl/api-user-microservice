from abc import ABC, abstractmethod
from src.application.dtos.user_dto import UserDto

class IndexUserByIdUseCaseInterface(ABC):
  @abstractmethod
  def execute(self, user_id: str) -> UserDto:
    pass
