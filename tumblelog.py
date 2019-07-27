from mongoengine import *

connect('tumblelog')


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comment = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()



for post in Post.objects:
    print(post.title)
    print('=' * len(post.title))
    if isinstance(post, TextPost):
            print(post.content)
    if isinstance(post, LinkPost):
            print('Link {}'.format(post.link_url))
    print()
    print()
