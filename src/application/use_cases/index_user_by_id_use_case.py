from injector import inject
from src.application.interfaces.use_cases.index_user_by_id_use_case_interface import IndexUserByIdUseCaseInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.dtos.user_dto import UserDto

class IndexUserByIdUseCase(IndexUserByIdUseCaseInterface):
  @inject
  def __init__(self, user_repository: UserRepositoryInterface) -> None:
    self.user_repository = user_repository

  def execute(self, user_id: str) -> UserDto:
    user_dto = self.user_repository.index_by_id(user_id)

    if not user_dto:
      raise RuntimeError()

