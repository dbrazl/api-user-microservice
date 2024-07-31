from abc import ABC, abstractmethod

class EnvironmentManagerInterface(ABC):
  @abstractmethod
  def listen_dev_db_changes(self):
    pass
