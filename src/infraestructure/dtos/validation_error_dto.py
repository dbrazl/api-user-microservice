from typing import Any

class ValidationErrorDto:
  def __init__(self, message: str, errors: str) -> None:
    self.message = message
    self.errors = errors

  def to_dict(self) -> dict[str, Any]:
    errors = list(map(lambda error: { "messsage": error["msg"], "field": error["loc"][0] }, self.errors))

    return {
      "error": self.message,
      "errors": errors
    }
