from flask import Blueprint, make_response
from src.core.interfaces.http_status_interface import HttpStatusInterface

class UserController:
  user_bp = Blueprint('user_bp', __name__)

  @staticmethod
  @user_bp.route('/health', methods=['GET'])
  def health(http_status: HttpStatusInterface):
    return make_response('', http_status.OK)
