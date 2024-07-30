import os

class Config:
  PORT = os.getenv('PORT')
  ENVIRONMENT = os.getenv('ENVIRONMENT')
  VERSION = os.getenv('API_VERSION')
