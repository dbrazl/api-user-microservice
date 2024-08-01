from injector import inject
from src.application.interfaces.use_cases.index_user_by_id_use_case_interface import IndexUserByIdUseCaseInterface
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.exceptions.api_exception import ApiException
from src.application.dtos.user_dto import UserDto

class IndexUserByIdUseCase(IndexUserByIdUseCaseInterface):
  @inject
  def __init__(
    self,
    user_repository: UserRepositoryInterface,
    http_status: HttpStatusInterface,
    exception_messages: ExceptionMessagesInterface
  ) -> None:
    self.user_repository = user_repository
    self.http_status = http_status
    self.exception_messages = exception_messages

  def execute(self, user_id: str) -> UserDto:
    user_dto = self.user_repository.index_by_id(user_id)

    if not user_dto:
      raise ApiException(message=self.exception_messages.USER_NOT_FOUND, status_code=self.http_status.INTERNAL_SERVER_ERROR)

    return user_dto
