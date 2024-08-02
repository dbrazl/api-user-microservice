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

  @property
  @abstractmethod
  def UNEXPECTED_FILTERS() -> str:
    pass

  @property
  @abstractmethod
  def DO_NOT_USE_ID_AND_EMAIL_FILTER_TOGETHER() -> str:
    pass

  @property
  @abstractmethod
  def VALIDATION_ERROR() -> str:
    pass
