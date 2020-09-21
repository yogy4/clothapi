from app import db
from conf.base import make_response, request, jwt_required, jsonify
from models import Transaction



@jwt_required
def read_one(member_id):
    try:
        tr = Transaction.query.filter_by(member_id = member_id).first()
        return jsonify(tr.history())
    except Exception as e:
        return (str(e))

