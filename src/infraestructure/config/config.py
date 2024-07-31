import os

class Config:
  PORT = os.getenv('PORT')
  ENVIRONMENT = os.getenv('ENVIRONMENT')
  API_VERSION = os.getenv('API_VERSION')
  DATABASE_URL = os.getenv('DATABASE_URL')
