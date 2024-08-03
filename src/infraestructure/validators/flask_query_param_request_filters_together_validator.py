from functools import wraps
from flask import request, current_app
from src.application.exceptions.api_exception import ApiException
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface

def flask_query_param_request_filters_together_validator(function):
  @wraps(function)
  def check(*args, **kwargs):
    query_params = request.args

    if query_params:
      filters = request.args.keys()

      if len(filters) > 1:
        exception_messages: ExceptionMessagesInterface = current_app.injector.get(ExceptionMessagesInterface)
        http_status: HttpStatusInterface = current_app.injector.get(HttpStatusInterface)
        raise ApiException(message=exception_messages.DO_NOT_USE_FILTERS_TOGETHER, status_code=http_status.BAD_REQUEST)

    return function(*args, **kwargs)

  return check

