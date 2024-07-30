from dotenv import load_dotenv
load_dotenv()
import os

from src.main.server.server import Server

if __name__ == '__main__':
  Server().listen(port=os.getenv('PORT'), env=os.getenv('ENVIRONMENT'))
