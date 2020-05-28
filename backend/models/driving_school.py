from mongoengine import EmbeddedDocument, StringField, IntField, ListField, DictField

class DrivingSchool(EmbeddedDocument):
	nit_driving_school = StringField(required=True)
	name = StringField(required=True)