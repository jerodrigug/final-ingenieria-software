from mongoengine import Document, StringField

class DrivingSchool(Document):
	nit_driving_school = StringField(required=True, unique=True)
	name = StringField(required=True)
	email = StringField(max_length=50, unique=True, required=True)
	address = StringField(required=True)