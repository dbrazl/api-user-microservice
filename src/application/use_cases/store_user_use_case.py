from injector import inject
from src.application.dtos.user_dto import UserDto
from src.application.interfaces.use_cases.store_user_use_case_interface import StoreUserUseCaseInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface

class StoreUserUseCase(StoreUserUseCaseInterface):
  @inject
  def __init__(self, user_repository: UserRepositoryInterface) -> None:
    self.user_repository = user_repository

  def execute(self, user: UserDto) -> None:
    self.user_repository.store(user)
