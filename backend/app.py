from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

import config

# Routes

from routes.user import user_routes
from routes.driving_school import driving_school_routes
from routes.document import document_routes

# Helpers

from helpers.helper import * 

app = Flask(__name__)
app.config['MONGODB_HOST'] = config.DB_URI
app.url_map.strict_slashes = False

app.register_blueprint(user_routes)
app.register_blueprint(driving_school_routes)
app.register_blueprint(document_routes)

db = MongoEngine(app)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)