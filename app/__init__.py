from flask import Flask

from .models import db, Engagement, Service, Application
from .views import default

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

app.register_blueprint(default)
db.init_app(app)
