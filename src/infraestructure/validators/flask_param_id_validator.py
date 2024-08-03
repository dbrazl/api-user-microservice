from functools import wraps
from flask import request
from src.infraestructure.dtos.pydantic_id_dto import PydanticIdDto

def flask_param_id_validator(function):
  @wraps(function)
  def check(*args, **kwargs):
    id = kwargs.get('id')
    PydanticIdDto(id=id)
    return function(*args, **kwargs)

  return check

