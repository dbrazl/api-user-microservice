from functools import wraps
from flask import request
from src.infraestructure.dtos.pydantic_name_dto import PydanticNameDto

def flask_check_name_validator(function):
  @wraps(function)
  def check(*args, **kwargs):
    name = request.args.get('name')

    if name:
      PydanticNameDto(name=name)

    return function(*args, **kwargs)

  return check

