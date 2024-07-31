from abc import ABC, abstractmethod

class DatabaseSchemaInterface(ABC):
  @abstractmethod
  def create_base_schema(self):
    pass
