from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fjkdlsbafd134klfjsda323435cjkldfsa'

from personal_site import routes
