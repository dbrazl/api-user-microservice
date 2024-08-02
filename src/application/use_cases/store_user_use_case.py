from injector import inject
from src.application.dtos.user_dto import UserDto
from src.application.interfaces.use_cases.store_user_use_case_interface import StoreUserUseCaseInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface
from src.application.exceptions.api_exception import ApiException

class StoreUserUseCase(StoreUserUseCaseInterface):
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

  def execute(self, user: UserDto) -> None:
    user_already_exist = self.user_repository.index_by_email(user.email)

    if user_already_exist:
      raise ApiException(message=self.exception_messages.USER_ALREADY_EXIST, status_code=self.http_status.UNAUTHORIZED)

    self.user_repository.store(user)
