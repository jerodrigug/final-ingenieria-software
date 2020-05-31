from flask import Blueprint, request, jsonify

from models.user import User

import auth

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = User.check_credentials(email, password)
    
    if not user:
        return jsonify({'msg': 'Incorrect email or password'}), 404

    return jsonify({'user': user})


@user_routes.route('/register_user', methods=['POST'])
def register():
    try:

        user = User(
            id_number=request.form['id_number'],
            nit_driving_school=request.form['nit_driving_school'],
            name=request.form['name'],
            last_name=request.form['last_name'],
            email=request.form['email'],
            password=auth.encrypt_password(request.form['password']),
            is_admin=request.form['is_admin']
        )

        user.save()

        return jsonify({'user': user}), 200

    except:
        
        return jsonify({'msg': 'No se ha podido registrar el usuario.'}), 500