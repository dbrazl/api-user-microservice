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

  @property
  @abstractmethod
  def RESOURCE_NOT_FOUNDED() -> str:
    pass

  @property
  @abstractmethod
  def METHOD_NOT_ALLOWED() -> str:
    pass
