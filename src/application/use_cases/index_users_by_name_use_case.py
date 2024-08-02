from injector import inject
from src.application.interfaces.use_cases.index_users_by_name_use_case_interface import IndexUsersByNameUseCaseInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.dtos.user_dto import UserDto

class IndexUsersByNameUseCase(IndexUsersByNameUseCaseInterface):
  @inject
  def __init__(self, user_repository: UserRepositoryInterface) -> None:
    self.user_repository = user_repository

  def execute(self, name: str) -> list[UserDto]:
    return self.user_repository.index_by_name(name)
