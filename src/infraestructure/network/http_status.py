from src.application.interfaces.network.http_status_interface import HttpStatusInterface

class HttpStatus(HttpStatusInterface):
  OK = 200
  CREATED = 201
  NO_CONTENT = 204
  BAD_REQUEST = 400
  UNAUTHORIZED = 401
  NOT_FOUND = 404
  INTERNAL_SERVER_ERROR = 500
  METHOD_NOT_ALLOWED = 405
