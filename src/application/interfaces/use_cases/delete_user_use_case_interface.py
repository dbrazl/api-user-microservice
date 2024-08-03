from abc import ABC, abstractmethod

class DeleteUserUseCaseInterface(ABC):
  @abstractmethod
  def execute(self, user_id: str) -> None:
    pass
