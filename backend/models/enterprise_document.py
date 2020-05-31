from mongoengine import Document, StringField, BooleanField

class EnterpriseDocument(Document):
	nit_driving_school = StringField(required=True)
	name = StringField(required=True, unique=True)
	location = StringField(required=True, unique=True)
	date = StringField(required=True)
	authenticated = BooleanField(default=False, required=True)