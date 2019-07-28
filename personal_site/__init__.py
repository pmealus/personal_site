from flask import Flask
from mongoengine import connect
from personal_site import models

app = Flask(__name__)
connect('personal_site_dev')

app.config['SECRET_KEY'] = 'fjkdlsbafd134klfjsda323435cjkldfsa'

from personal_site import routes
