from flask import Blueprint, request, jsonify

from models.driving_school import DrivingSchool

driving_school_routes = Blueprint('driving_school_routes', __name__)

@driving_school_routes.route('/register_driving_school', methods=['POST'])
def register_driving_school():
    try:
        driving_school = DrivingSchool(
            nit_driving_school = request.form['nit_driving_school'],
            name = request.form['name']
        )

        driving_school.save()

        return jsonify({'driving_school': driving_school})

    except:
        
        return jsonify({'msg': 'NIT already taken'}), 500