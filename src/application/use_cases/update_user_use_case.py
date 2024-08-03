from injector import inject
from src.application.dtos.user_dto import UserDto
from src.application.interfaces.use_cases.update_user_use_case_interface import UpdateUserUseCaseInterface
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface
from src.application.exceptions.api_exception import ApiException

class UpdateUserUseCase(UpdateUserUseCaseInterface):
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
    user_exist = self.user_repository.index_by_id(user.id)

    if not user_exist:
      raise ApiException(message=self.exception_messages.USER_NOT_FOUND, status_code=self.http_status.UNAUTHORIZED)

    user_email_owner = self.user_repository.index_by_email(user.email)
    user_email_already_in_use = user_email_owner and user_email_owner.id != user.id

    if user_email_already_in_use:
      raise ApiException(message=self.exception_messages.USER_EMAIL_ALREADY_IN_USE, status_code=self.http_status.UNAUTHORIZED)

    self.user_repository.update(user)
