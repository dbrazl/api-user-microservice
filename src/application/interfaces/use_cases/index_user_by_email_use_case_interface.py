from abc import ABC, abstractmethod
from src.application.dtos.user_dto import UserDto

class IndexUserByEmailUseCaseInterface(ABC):
  @abstractmethod
  def execute(self, user_email: str) -> UserDto:
    pass
