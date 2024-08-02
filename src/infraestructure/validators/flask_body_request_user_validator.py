from functools import wraps
from flask import request
from src.infraestructure.dtos.pydantic_user_dto import PydanticUserDto

def flask_body_request_user_validator(function):
  @wraps(function)
  def check(*args, **kwargs):
    body = request.get_json()
    PydanticUserDto(**body)
    return function(*args, **kwargs)

  return check

