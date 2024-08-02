from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface

class ExceptionMessages(ExceptionMessagesInterface):
  INTERNAL_SERVER_ERROR = 'Internal server error. Try again!'
  USER_NOT_FOUND = 'User not founded'
  RESOURCE_NOT_FOUNDED = 'Resource not founded'
  METHOD_NOT_ALLOWED = 'Method not allowed. Check URL and HTTP verb'
  UNEXPECTED_FILTERS = 'The endpoint receive unexpected filters. Check the query params'
  DO_NOT_USE_ID_AND_EMAIL_FILTER_TOGETHER = 'Do not use id and email filter together'
  VALIDATION_ERROR = 'Validation error'
  USER_ALREADY_EXIST = 'User already exist'
