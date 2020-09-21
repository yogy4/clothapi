from flask import Blueprint
from controllers.cloth import get_all_cloth, get_one_cloth, update_cloth, create_cloth, delete_cloth
from controllers.member import register, login
from controllers.transaction import get_one_transc, get_all_transc, create_transc, delete_transc
from controllers.history import read_one

controller = Blueprint('controller', 'controllers', url_prefix='/api')
controller.add_url_rule('/registration', view_func=register, methods=['POST'])
controller.add_url_rule('/login', view_func=login, methods=['POST'])

controller.add_url_rule('/cloths', view_func=get_all_cloth, methods=['GET'])
controller.add_url_rule('/cloth', view_func=create_cloth, methods=['POST'])
controller.add_url_rule('/cloth/:id', view_func=update_cloth, methods=['PUT'])
controller.add_url_rule('/cloth/:id', view_func=get_one_cloth, methods=['GET'])
controller.add_url_rule('/cloth/:id', view_func=delete_cloth, methods=['DELETE'])

controller.add_url_rule('/transactions', view_func=get_all_transc, methods=['GET'])
controller.add_url_rule('/transaction', view_func=get_one_transc, methods=['GET'])
controller.add_url_rule('/transaction', view_func=create_transc, methods=['POST'])
controller.add_url_rule('/transaction/:id', view_func=delete_transc, methods=['DELETE'])

controller.add_url_rule('/history/:member_id', view_func=read_one, methods=['GET'])