from abc import ABC, abstractmethod

class ExceptionMessagesInterface(ABC):
  @property
  @abstractmethod
  def INTERNAL_SERVER_ERROR() -> str:
    pass

  @property
  @abstractmethod
  def USER_NOT_FOUND() -> str:
    pass
