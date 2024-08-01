from abc import ABC, abstractmethod

class HttpStatusInterface(ABC):
  @property
  @abstractmethod
  def OK() -> int:
    pass

  @property
  @abstractmethod
  def INTERNAL_SERVER_ERROR() -> int:
    pass
