class ApiException(Exception):
  def __init__(self, message: str, status_code: str) -> None:
    self.message = message
    self.status_code = status_code
