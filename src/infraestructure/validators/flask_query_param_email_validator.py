from functools import wraps
from flask import request
from src.infraestructure.dtos.pydantic_email_dto import PydanticEmailDto

def flask_query_param_email_validator(function):
  @wraps(function)
  def check(*args, **kwargs):
    email = request.args.get('email')

    if email:
      PydanticEmailDto(email=email)

    return function(*args, **kwargs)

  return check

