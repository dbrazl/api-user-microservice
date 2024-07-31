from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
  @abstractmethod
  def index(self):
    pass

  @abstractmethod
  def index_one(self, user_id):
    pass

  @abstractmethod
  def index_by_email(self, user_email):
    pass

  @abstractmethod
  def store(self, user):
    pass

  @abstractmethod
  def update(self, user):
    pass

  @abstractmethod
  def delete(self, user_id):
    pass
