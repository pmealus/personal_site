from mongoengine import *


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField()
    comment = ListField(EmbeddedDocumentField(Comment))

