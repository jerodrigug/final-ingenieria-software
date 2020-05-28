import auth

from mongoengine import Document, StringField, BooleanField

class User(Document):
	id_number = StringField(max_length=15, unique=True, required=True)
	name = StringField(max_length=50, required=True)
	last_name = StringField(max_length=50, required=True)
	email = StringField(max_length=50, unique=True, required=True)
	password = StringField(required=True)
	is_admin = BooleanField(default=False, required=True)
	nit_driving_school = StringField(required=True)

	@classmethod
	def check_credentials(cls, email, password):
		user = cls.objects(email=email) # Lista con usuarios que cumplan dicha condición

		if not user: # El usuario no está registrado
			return False

		login = auth.check_encrypted_password(password, user[0].password)

		if not login: # La contraseña es incorrecta
			return False

		return user[0] # El usuario se ha autenticado con éxito, se retorna la información del usuario