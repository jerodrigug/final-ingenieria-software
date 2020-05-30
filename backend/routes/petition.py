from flask import Blueprint, request, jsonify

from models.petition import Petition

petition_routes = Blueprint('petition_routes', __name__)

@petition_routes.route('/register_petition', methods=['POST'])
def register_petition():
    try:
        petiton = Petition(
            nit_driving_school = request.form['nit_driving_school'],
            document = request.form['document'],
            state_entity = request.form['state_entity'],
            date = request.form['date']
        )

        petiton.save()

        return jsonify({'petiton': petiton})

    except:
        
        return jsonify({'msg': 'Error with petition'}), 500