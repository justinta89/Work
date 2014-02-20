from flask.ext.wtf import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Length

# from .models import Sample


class EngagementForm(Form):
    validators = [DataRequired(), Length(min=3, max=250)]
    name = StringField('name', validators=validators)
