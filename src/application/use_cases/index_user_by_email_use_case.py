from injector import inject
from application.dtos.user_dto import UserDto
from src.application.interfaces.use_cases.index_user_by_email_use_case_interface import IndexUserByEmailUseCaseInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.exceptions.api_exception import ApiException

class IndexUserByEmailUseCase(IndexUserByEmailUseCaseInterface):
  @inject
  def __init__(
    self,
    user_repository: UserRepositoryInterface,
    exception_messages: ExceptionMessagesInterface,
    http_status: HttpStatusInterface
  ) -> None:
    self.user_repository = user_repository
    self.exception_messages = exception_messages
    self.http_status = http_status

  def execute(self, user_email: str) -> UserDto:
    user_dto = self.user_repository.index_by_email(user_email)

    if not user_dto:
      raise ApiException(message=self.exception_messages.USER_NOT_FOUND, status_code=self.http_status.NOT_FOUND)

    return user_dto
