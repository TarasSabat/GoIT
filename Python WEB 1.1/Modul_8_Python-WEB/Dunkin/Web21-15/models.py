from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import (
    EmbeddedDocumentField,
    ListField, 
    StringField, 
    DateTimeField,
    )


class Vaccine(EmbeddedDocument):
    vaccine_date = DateTimeField(required=True)
    vaccine_name = StringField()


class Cat(Document):
    name = StringField()
    color = StringField()
    vaccines = ListField(EmbeddedDocumentField(Vaccine))