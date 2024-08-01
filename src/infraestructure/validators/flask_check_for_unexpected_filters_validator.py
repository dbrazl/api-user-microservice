from functools import wraps
from flask import request, current_app
from src.application.exceptions.api_exception import ApiException
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface

def flask_check_for_unexpected_filters_validator(function):
  @wraps(function)
  def check(*args, **kwargs):
    query_params = request.args
    allowed_params = {'id', 'email'}

    extra_params = set(query_params.keys()) - allowed_params

    if extra_params:
      exception_messages: ExceptionMessagesInterface = current_app.injector.get(ExceptionMessagesInterface)
      http_status: HttpStatusInterface = current_app.injector.get(HttpStatusInterface)
      raise ApiException(message=exception_messages.UNEXPECTED_FILTERS, status_code=http_status.BAD_REQUEST)

    return function(*args, **kwargs)

  return check

