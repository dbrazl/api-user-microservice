from injector import inject
from src.application.interfaces.use_cases.delete_user_use_case_interface import DeleteUserUseCaseInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface

class DeleteUserUseCase(DeleteUserUseCaseInterface):
  @inject
  def __init__(self, user_repository: UserRepositoryInterface) -> None:
    self.user_repository = user_repository

  def execute(self, user_id: str) -> None:
    self.user_repository.delete(user_id)
