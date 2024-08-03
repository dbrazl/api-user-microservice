from abc import ABC, abstractmethod
from src.application.dtos.user_dto import UserDto

class UserControllerInterface(ABC):
  @abstractmethod
  def health(self) -> None:
    pass

  @abstractmethod
  def index(self, filter: str, filter_value: str) -> list[UserDto] | UserDto:
    pass

  @abstractmethod
  def store(self, user: UserDto) -> None:
    pass

  @abstractmethod
  def update(self, user: UserDto) -> None:
    pass

  @abstractmethod
  def delete(self, user_id: str) -> None:
    pass
