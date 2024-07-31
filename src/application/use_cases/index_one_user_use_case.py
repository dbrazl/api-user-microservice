from injector import inject
from src.application.interfaces.use_cases.index_one_user_use_case_interface import IndexOneUserUseCaseInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface

class IndexOneUserUseCase(IndexOneUserUseCaseInterface):
  @inject
  def __init__(self, user_repository: UserRepositoryInterface):
    self.user_repository = user_repository

  def execute(self, user_id):
    return self.user_repository.index_one(user_id)
