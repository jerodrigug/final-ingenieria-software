from mongoengine import EmbeddedDocument, StringField

class Petition(EmbeddedDocument):
	nit_driving_school = StringField(required=True)
	document = StringField(required=True)
	state_entity = StringField(required=True)
	date = StringField(required=True)