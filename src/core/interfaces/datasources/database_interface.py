from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
  @abstractmethod
  def connect(self):
    pass
