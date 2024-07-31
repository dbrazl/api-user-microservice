from abc import ABC, abstractmethod

class IndexOneUserUseCaseInterface(ABC):
  @abstractmethod
  def execute(self, user_id):
    pass
