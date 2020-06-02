import requests
import config

from flask import Blueprint, request, jsonify
from datetime import datetime

from mongoengine import Document

# Helpers

from helpers.helper import * 

# Models

from models.enterprise_document import EnterpriseDocument

document_routes = Blueprint('document_routes', __name__)

@document_routes.route('/upload_unauthenticated_document', methods=['POST'])
def upload_unauthenticated_document():
	if 'user_file' not in request.files:
		return jsonify({'msg': 'No se encontró el archivo.'}), 500

	file = request.files['user_file']

	if file.filename == '':
		return jsonify({'msg': 'Por favor selecciona un archivo.'}), 500

	if file:
		uploaded_document_location = upload_file_to_s3(file)
		
		try:
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")

			enterprise_document = EnterpriseDocument(
				nit_driving_school=str(request.form['nit_driving_school']),
				name=file.filename,
				location=uploaded_document_location,
				date=current_time,
				authenticated=False
			)

			enterprise_document.save()

			return jsonify({'uploaded_document_location': str(uploaded_document_location)}), 200

		except:

			return jsonify({'msg': 'No se pudo agregar el documento a la base de datos.'})


@document_routes.route('/authenticate_document', methods=['POST'])
def authenticate_document():

	get_status_code = int(requests.get(config.API_BASE_URL + '/apis/authenticateDocument/' + str(request.form['nit_driving_school']) 
		+ '/' + str(request.form['location']) + '/' + str(request.form['name'])).status_code)

	if get_status_code == 200:
		try:
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")

			enterprise_document = EnterpriseDocument(
				nit_driving_school=str(request.form['nit_driving_school']) ,
				name=str(request.form['name']),
				location=str(request.form['location']),
				date=current_time,
				authenticated=True
			)

			enterprise_document.update()

			return jsonify({'enterprise_authenticated_document': enterprise_authenticated_document}), 200

		except:

			return jsonify({'msg': 'No se ha podido autenticar el documento.'}), 500

	return jsonify({'msg': 'No se ha podido autenticar el documento.'}), 500

@document_routes.route('/documents', methods=['GET'])
def get_all_documents():
	return jsonify({'documents': EnterpriseDocument.objects()})