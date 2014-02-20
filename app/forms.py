from flask.ext.wtf import Form
from wtforms.fields import (StringField, SelectField, BooleanField, DateField,
                            DecimalField, TextField, TextAreaField)
from wtforms.validators import DataRequired, Length, NumberRange, URL, Optional

from app import constants
from .models import Engagement, Application, API, NetworkLayer, Perspective


class EngagementForm(Form):
    choices = [(choice, choice) for choice in constants.ENGAGEMENT_TYPES]
    type = SelectField(choices=choices)

    renewal = BooleanField()
    number_of_reports = DecimalField(validators=[Optional(),
                                                 NumberRange(min=0, max=100)])
    retesting_hours = DecimalField(validators=[Optional(),
                                               NumberRange(min=0, max=1000)])

    # Constraints
    choices = [(choice, choice) for choice in constants.REPORTING_FREQUENCY]
    reporting_frequency = SelectField(choices=choices)

    time_window = TextField(Length(max=500))
    deadline = DateField(validators=[Optional()])

    choices = [(choice, choice) for choice in constants.APPLIANCES]
    security_appliances = SelectField(choices=choices)

    permit_whitelisting = BooleanField()
    bandwidth_restrictions = TextField()
    uses_third_parties = BooleanField()
    thid_parties = TextField()
    past_issues = BooleanField()
    notes = TextAreaField()


class ApplicationForm(Form):
    link = TextField(validators=[URL()])
    non_auth_assessment = BooleanField()
    requires_auth = BooleanField()
    role_count = DecimalField()
    public_registration = BooleanField()

    choices = [(choice, choice) for choice in constants.SIZE_OF_APPLICATION]
    size = SelectField(choices=choices)

    # Constraints
    blacklisted_pages = TextField()
    requires_two_factor = BooleanField()
    two_factor_methods = TextField()
    live_database = BooleanField()

    choices = [(choice, choice) for choice in constants.REPORTING_FREQUENCY]
    reporting_frequency = SelectField(choices=choices)

    time_window = TextField(Length(max=500))
    deadline = DateField()

    choices = [(choice, choice) for choice in constants.APPLIANCES]
    security_appliances = SelectField(choices=choices)

    permit_whitelisting = BooleanField()
    bandwidth_restrictions = TextField()
    uses_third_parties = BooleanField()
    thid_parties = TextField()
    past_issues = BooleanField()
    notes = TextAreaField()
