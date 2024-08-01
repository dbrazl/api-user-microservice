from src.application.interfaces.network.http_status_interface import HttpStatusInterface

class HttpStatus(HttpStatusInterface):
  OK = 200
  NOT_FOUND = 404
  INTERNAL_SERVER_ERROR = 500
