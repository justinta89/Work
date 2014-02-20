from flask.ext.wtf import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Length, NumberRange

import constants
from .models import Engagement, Application, API, Network, Perspective


class EngagementForm(Form):
    type = SelectField(choices=constants.ENGAGEMENT_TYPES)
    renewal = BooleanField()
    number_of_reports = DecimalField(validator=[NumberRange(min=0, max=100)])
    retesting_hours = DecimalField(validator=[NumberRange(min=0, max=1000)])

    # Constraints
    reporting_frequency = SelectField(choices=constants.REPORTING_FREQUENCY)
    time_window = TextField(Length(max=500))
    deadline = DateField()
    security_appliances = SelectField(choices=constants.APPLIANCES)
    permit_whitelisting = BooleanField()
    bandwidth_restrictions = TextField()
    uses_third_parties = BooleanField()
    thid_parties = TextField()
    past_issues = BooleanField()
    notes = TextArea()


class ApplicationForm(Form):
    link = TextField(validator=[URL()])
    non_auth_assessment = BooleanField()
    requires_auth = BooleanField()
    role_count = DecimalField()
    public_registration = BooleanField()
    size = SelectField(choices=constants.SIZE_OF_APPLICATION)

    # Constraints
    blacklisted_pages = TextField()
    requires_two_factor = BooleanField()
    two_factor_methods = TextField()
    live_database = BooleanField()

    reporting_frequency = SelectField(choices=constants.REPORTING_FREQUENCY)
    time_window = TextField(Length(max=500))
    deadline = DateField()
    security_appliances = SelectField(choices=constants.APPLIANCES)
    permit_whitelisting = BooleanField()
    bandwidth_restrictions = TextField()
    uses_third_parties = BooleanField()
    thid_parties = TextField()
    past_issues = BooleanField()
    notes = TextArea()
