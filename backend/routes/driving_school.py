import requests
import config

from flask import Blueprint, request, jsonify

from models.driving_school import DrivingSchool

driving_school_routes = Blueprint('driving_school_routes', __name__)

@driving_school_routes.route('/register_driving_school', methods=['POST'])
def register_driving_school():
	try:
		driving_school = DrivingSchool(
			nit_driving_school = request.form['nit_driving_school'],
			name = request.form['name'],
			email = request.form['email'],
			address = request.form['address']
		)

		response_status_code = int(requests.get(config.API_BASE_URL + '/apis/validateCitizen/' + str(request.form['nit_driving_school'])).status_code)
		
		if response_status_code == 200:

			post_data = {
  				'id': request.form['nit_driving_school'],
  				'name': request.form['name'],
  				'address': request.form['address'],
  				'email': request.form['email'],
  				'operatorId': 2020,
  				'operatorName': 'CarpeTransit'
			}	

			post_status_code = requests.post(config.API_BASE_URL + '/apis/registerCitizen', data=post_data).status_code
			
			if post_status_code == 200:
				driving_school.save()
				return jsonify({'driving_school': driving_school}), 200
			
	except:
		return jsonify({'msg': 'Problemas al registrar la escuela.'}), 500