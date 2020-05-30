from mongoengine import Document, EmbeddedDocument, StringField, IntField, ListField, DictField

class DrivingSchool(Document):
	nit_driving_school = StringField(required=True, unique=True)
	name = StringField(required=True)