from abc import ABC, abstractmethod
from src.application.dtos.user_dto import UserDto

class UserRepositoryInterface(ABC):
  @abstractmethod
  def index(self) -> list[UserDto]:
    pass

  @abstractmethod
  def index_one(self, user_id: str) -> UserDto:
    pass

  @abstractmethod
  def index_by_email(self, user_email: str) -> UserDto:
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
