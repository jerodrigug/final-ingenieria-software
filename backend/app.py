from flask import Flask, flash, request, redirect, url_for, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine

# Models
from models.user import User
from models.driving_school import DrivingSchool
from models.petition import Petitio

# Routes
from routes.user import user_routes
from routes.driving_school import driving_school_routes
from routes.petition import petition_routes

import config

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['MONGODB_HOST'] = config.DB_URI

app.register_blueprint(user_routes)
app.register_blueprint(driving_school_routes)
app.register_blueprint(petition_routes)

db = MongoEngine(app)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)