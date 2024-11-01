from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface

class ExceptionMessages(ExceptionMessagesInterface):
  INTERNAL_SERVER_ERROR = 'Internal server error. Try again!'
  USER_NOT_FOUND = 'User not founded'
  RESOURCE_NOT_FOUNDED = 'Resource not founded'
  METHOD_NOT_ALLOWED = 'Method not allowed. Check URL and HTTP verb'
  UNEXPECTED_FILTERS = 'The endpoint receive unexpected filters. Check the query params'
  DO_NOT_USE_FILTERS_TOGETHER = 'Do not use different filters together. Choose one'
  VALIDATION_ERROR = 'Validation error'
  USER_ALREADY_EXIST = 'The data provided cannot be used. Please try with different information'
  USER_EMAIL_ALREADY_IN_USE = 'The email provided cannot be used. Please use a different email'
