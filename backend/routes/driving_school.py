import requests

from flask import Blueprint, request, jsonify

from models.driving_school import DrivingSchool

driving_school_routes = Blueprint('driving_school_routes', __name__)

@driving_school_routes.route('/register_driving_school', methods=['POST'])
def register_driving_school():
	try:
		driving_school = DrivingSchool(nit_driving_school = request.form['nit_driving_school'], name = request.form['name'])
		
		response_status_code = int(requests.get('http://govcarpetaapp.mybluemix.net/apis/validateCitizen/' + str(request.form['nit_driving_school'])).status_code)
		
		if response_status_code == 200:
			driving_school.save()
			return jsonify({'msg': 'Se ha registrado la escuela de manera satisfactoria.'})
		
		else:
			return jsonify({'msg': 'No se pudo completar. La escuela ya está registrada en otro operador.'}), 500
	
	except:
		return jsonify({'msg': 'La escuela ya está registrada en este operador.'}), 500