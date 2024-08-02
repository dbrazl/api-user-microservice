from abc import ABC, abstractmethod

class HttpStatusInterface(ABC):
  @property
  @abstractmethod
  def OK() -> int:
    pass

  @property
  @abstractmethod
  def NO_CONTENT() -> int:
    pass

  @property
  @abstractmethod
  def BAD_REQUEST() -> int:
    pass

  @property
  @abstractmethod
  def UNAUTHORIZED() -> int:
    pass

  @property
  @abstractmethod
  def NOT_FOUND() -> int:
    pass

  @property
  @abstractmethod
  def METHOD_NOT_ALLOWED() -> int:
    pass

  @property
  @abstractmethod
  def INTERNAL_SERVER_ERROR() -> int:
    pass
