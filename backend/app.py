from flask import Flask, flash, request, redirect, url_for, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine

import requests
import config

#from boto.s3.connection import S3Connection
#from boto.s3.key import Key as S3Key

# Models
from models.user import User
from models.driving_school import DrivingSchool
from models.petition import Petition

# Routes
from routes.user import user_routes
from routes.driving_school import driving_school_routes
from routes.petition import petition_routes

app = Flask(__name__)

app.config['MONGODB_HOST'] = config.DB_URI
app.config['S3_BUCKET_NAME'] = 'software-final'
app.config['API_BASE_URL'] = 'http://govcarpetaapp.mybluemix.net'

app.url_map.strict_slashes = False

app.register_blueprint(user_routes)
app.register_blueprint(driving_school_routes)
app.register_blueprint(petition_routes)

db = MongoEngine(app)
CORS(app)

'''@app.route("/", methods=["POST"])
def upload_file():
	data_file = request.files..get('file')
    file_name = data_file.filename
    conection = S3Connection(config.ACCESS_KEY, config.SECRET_KEY)
    bucket = conection.get_bucket(config.BUCKET_NAME)
    key_bucket = Key(bucket)
    key_bucket.key = 'file_test.jpg'
    key_bucket.set_contents_from_string(data_file.read())

    return jsonify(name=file_name)
	'''
if __name__ == '__main__':
    app.run(debug=True)