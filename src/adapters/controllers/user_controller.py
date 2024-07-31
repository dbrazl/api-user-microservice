from flask import Blueprint, make_response, jsonify
from src.adapters.models.user_response_dto import UserResponseDto
from src.adapters.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.use_cases.index_one_user_use_case_interface import IndexOneUserUseCaseInterface

class UserController:
  user_bp = Blueprint('user_bp', __name__)

  @staticmethod
  @user_bp.route('/health', methods=['GET'])
  def health(http_status: HttpStatusInterface):
    return make_response('', http_status.OK)

  @staticmethod
  @user_bp.route('/<string:user_id>', methods=['GET'])
  def index_one(user_id, http_status: HttpStatusInterface, index_one_user_use_case: IndexOneUserUseCaseInterface):
    return make_response('', http_status.OK)
