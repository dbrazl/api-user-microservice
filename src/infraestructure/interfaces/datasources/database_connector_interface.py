from abc import ABC, abstractmethod

class DatabaseConnectorInterface(ABC):
  @abstractmethod
  def connect(self):
    pass
