from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface

class ExceptionMessages(ExceptionMessagesInterface):
  INTERNAL_SERVER_ERROR = 'Internal server error. Try again!'
  USER_NOT_FOUND = 'User not founded'
  RESOURCE_NOT_FOUNDED = 'Resource not founded'
  METHOD_NOT_ALLOWED = 'Method not allowed. Check URL and HTTP verb'
