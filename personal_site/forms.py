import flask_wtforms

class ContactForm(inheritfromwtforms):
    name = StringField()
    email = EmailField()
    message = StringField()