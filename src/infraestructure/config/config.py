import os

class Config:
  PORT = os.getenv('PORT')
  ENVIRONMENT = os.getenv('ENVIRONMENT')
