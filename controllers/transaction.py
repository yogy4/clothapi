from app import db
# from flask import jsonify
from conf.base import make_response, request, jwt_required, jsonify
from models import Transaction

@jwt_required
def get_all_transc():
    try:
        tr = Transaction.query.all()
        return jsonify([e.serialize() for e in tr])
    except Exception as e:
        return (str(e))

@jwt_required
def get_one_transc(id_):
    try:
        tr = Transaction.query.filter_by(id = id_).first()
        return jsonify(tr.serialize())
    except Exception as e:
        return (str(e))

@jwt_required
def create_transc():
    post_data = request.get_json()
    if request.method == 'POST':
        try:
            tr = Transaction(
                member_id = post_data.get('member_id'),
                cloth = post_data.get('cloth'),
                quantity = post_data.get('quantity'),
                total_prices = post_data.get('total_prices')
            )
            db.session.add(tr)
            db.session.commit()
            resp = {
                'status': 'success',
                'message': 'successfully insert'
            }
            return make_response(jsonify(resp)), 201
        except Exception as e:
            # return (str(e))
            resp = {
                'status': 'fail',
                'message': 'some error occured' + e
            }
            return make_response(jsonify(resp)), 401


@jwt_required
def delete_transc(id):
    post_data = request.get_json()
    tr = Transaction.query.filter_by(id = post_data.get('id')).first()
    if not tr:
        if not isinstance(str):
            try:
                db.session.delete(tr)
                db.session.commit()
                return {
                    "message": "baju {} was deleted".format(tr.id)
                }
            except Exception as e:
                return (str(e))
