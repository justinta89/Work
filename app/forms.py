from flask.ext.wtf import Form
from wtforms.fields import (StringField, SelectField, BooleanField, DateField,
                            DecimalField, TextField, TextAreaField,
                            SelectMultipleField)
from wtforms.validators import DataRequired, Length, NumberRange, URL, Optional

from app import constants
from .models import Engagement, Application, API, NetworkLayer, Perspective


class EngagementForm(Form):
    choices = [(choice, choice) for choice in constants.ENGAGEMENT_TYPES]
    type = SelectField(constants.TYPE_LABEL, choices=choices)

    renewal = BooleanField(constants.RENEWAL_LABEL)
    number_of_reports = DecimalField(constants.NUMBER_OF_REPORTS_LABEL,
                                     validators=[Optional(),
                                                 NumberRange(min=0, max=100)])
    retesting_hours = DecimalField(constants.RETESTING_HOURS_LABEL,
                                   validators=[Optional(),
                                               NumberRange(min=0, max=1000)])

    # Constraints
    choices = [(choice, choice) for choice in constants.REPORTING_FREQUENCY]
    reporting_frequency = SelectField(constants.REPORTING_FREQUENCY_LABEL,
                                      choices=choices)

    time_window = TextField(constants.TIME_WINDOW_LABEL,
                            validators=[Length(max=500)])
    deadline = DateField(constants.DEADLINE_LABEL, validators=[Optional()])

    choices = [(choice, choice) for choice in constants.APPLIANCES]
    security_appliances = SelectMultipleField(
        constants.SECURITY_APPLIANCES_LABEL, choices=choices)

    permit_whitelisting = BooleanField(constants.PERMIT_WHITELISTING_LABEL)
    restrictions = TextField(constants.RESTRICTIONS_LABEL)
    bandwidth_restrictions = BooleanField(
        constants.BANDWIDTH_RESTRICTIONS_LABEL)
    uses_third_parties = BooleanField(constants.USES_THIRD_PARTIES_LABEL)
    third_parties = TextField(constants.THIRD_PARTIES_LABEL)
    past_issues = BooleanField(constants.PAST_ISSUES_LABEL)
    notes = TextAreaField(constants.NOTES_LABEL)


class ApplicationForm(Form):
    link = TextField(constants.LINK_LABEL, validators=[URL()])
    non_auth_assessment = BooleanField(constants.NON_AUTH_ASSESSMENT_LABEL)
    requires_auth = BooleanField(constants.REQUIRES_AUTH_LABEL)
    role_count = DecimalField(constants.ROLE_COUNT_LABEL)
    roles = TextField(constants.ROLES_LABEL)
    public_registration = BooleanField(constants.PUBLIC_REGISTRATION_LABEL)

    choices = [(choice, choice) for choice in constants.SIZE_OF_APPLICATION]
    size = SelectField(constants.SIZE_LABEL, choices=choices)

    # Constraints
    blacklisted_pages = TextField(constants.BLACKLISTED_PAGES_LABEL)
    requires_two_factor = BooleanField(constants.REQUIRES_TWO_FACTOR_LABEL)
    two_factor_methods = TextField(constants.TWO_FACTOR_METHODS_LABEL)
    live_database = BooleanField(constants.LIVE_DATABASE_LABEL)

    choices = [(choice, choice) for choice in constants.REPORTING_FREQUENCY]
    reporting_frequency = SelectField(constants.REPORTING_FREQUENCY_LABEL,
                                      choices=choices)

    time_window = TextField(constants.TIME_WINDOW_LABEL,
                            validators=[Length(max=500)])
    deadline = DateField(constants.DEADLINE_LABEL, validators=[Optional()])

    choices = [(choice, choice) for choice in constants.APPLIANCES]
    security_appliances = SelectMultipleField(
        constants.SECURITY_APPLIANCES_LABEL, choices=choices)

    permit_whitelisting = BooleanField(constants.PERMIT_WHITELISTING_LABEL)
    restrictions = TextField(constants.RESTRICTIONS_LABEL)
    bandwidth_restrictions = BooleanField(
        constants.BANDWIDTH_RESTRICTIONS_LABEL)
    uses_third_parties = BooleanField(constants.USES_THIRD_PARTIES_LABEL)
    third_parties = TextField(constants.THIRD_PARTIES_LABEL)
    past_issues = BooleanField(constants.PAST_ISSUES_LABEL)
    notes = TextAreaField(constants.NOTES_LABEL)


class APIForm(Form):
    link = TextField(constants.LINK_LABEL, validators=[URL()])
    non_auth_assessment = BooleanField(constants.NON_AUTH_ASSESSMENT_LABEL)
    requires_auth = BooleanField(constants.REQUIRES_AUTH_LABEL)
    role_count = DecimalField(constants.ROLE_COUNT_LABEL)
    roles = TextField(constants.ROLES_LABEL)
    public_registration = BooleanField(constants.PUBLIC_REGISTRATION_LABEL)

    choices = [(choice, choice) for choice in constants.SIZE_OF_APPLICATION]
    size = SelectField(constants.SIZE_LABEL, choices=choices)

    documentation = BooleanField(constants.DOCUMENTATION_LABEL,
                                 'Documentation Available')

    choices = [(choice, choice) for choice in constants.DOCUMENTATION_QUALITY]
    documentation_quality = SelectField(constants.DOCUMENTATION_QUALITY_LABEL,
                                        choices=choices)

    choices = [(choice, choice) for choice in constants.MESSAGE_FORMAT]
    message_format = SelectField(constants.MESSAGE_FORMAT_LABEL,
                                 choices=choices)

    prepopulated_objects = BooleanField(constants.PREPOPULATED_OBJECTS_LABEL)
    test_suites_available = BooleanField(constants.TEST_SUITES_AVAILABLE_LABEL)

    # Constraints
    os_specific = BooleanField(constants.OS_SPECIFIC_LABEL)
    requires_installation = BooleanField(constants.REQUIRES_INSTALLATION_LABEL)
    hardware_requirement = BooleanField(constants.HARDWARE_REQUIREMENT_LABEL)
    HMAC_required = BooleanField(constants.HMAC_REQUIRED)

    # Constraints
    blacklisted_pages = TextField(constants.BLACKLISTED_PAGES_LABEL)
    requires_two_factor = BooleanField(constants.REQUIRES_TWO_FACTOR_LABEL)
    two_factor_methods = TextField(constants.TWO_FACTOR_METHODS_LABEL)
    live_database = BooleanField(constants.LIVE_DATABASE_LABEL)

    choices = [(choice, choice) for choice in constants.REPORTING_FREQUENCY]
    reporting_frequency = SelectField(constants.REPORTING_FREQUENCY_LABEL,
                                      choices=choices)

    time_window = TextField(constants.TIME_WINDOW_LABEL,
                            validators=[Length(max=500)])
    deadline = DateField(constants.DEADLINE_LABEL, validators=[Optional()])

    choices = [(choice, choice) for choice in constants.APPLIANCES]
    security_appliances = SelectMultipleField(
        constants.SECURITY_APPLIANCES_LABEL, choices=choices)

    permit_whitelisting = BooleanField(constants.PERMIT_WHITELISTING_LABEL)
    restrictions = TextField(constants.RESTRICTIONS_LABEL)
    bandwidth_restrictions = BooleanField(
        constants.BANDWIDTH_RESTRICTIONS_LABEL)
    uses_third_parties = BooleanField(constants.USES_THIRD_PARTIES_LABEL)
    third_parties = TextField(constants.THIRD_PARTIES_LABEL)
    past_issues = BooleanField(constants.PAST_ISSUES_LABEL)
    notes = TextAreaField(constants.NOTES_LABEL)


class NetworkLayerForm(Form):
    scope = TextAreaField(constants.SCOPE_LABEL)
    unique_services = DecimalField(constants.UNIQUE_SERVICES_LABEL,
                                   validators=[Optional(), NumberRange(min=0)])

    # Constraints
    choices = [(choice, choice) for choice in constants.REPORTING_FREQUENCY]
    reporting_frequency = SelectField(constants.REPORTING_FREQUENCY_LABEL,
                                      choices=choices)

    time_window = TextField(constants.TIME_WINDOW_LABEL,
                            validators=[Length(max=500)])
    deadline = DateField(constants.DEADLINE_LABEL, validators=[Optional()])

    choices = [(choice, choice) for choice in constants.APPLIANCES]
    security_appliances = SelectMultipleField(
        constants.SECURITY_APPLIANCES_LABEL, choices=choices)

    permit_whitelisting = BooleanField(constants.PERMIT_WHITELISTING_LABEL)
    restrictions = TextField(constants.RESTRICTIONS_LABEL)
    bandwidth_restrictions = BooleanField(
        constants.BANDWIDTH_RESTRICTIONS_LABEL)
    uses_third_parties = BooleanField(constants.USES_THIRD_PARTIES_LABEL)
    third_parties = TextField(constants.THIRD_PARTIES_LABEL)
    past_issues = BooleanField(constants.PAST_ISSUES_LABEL)
    notes = TextAreaField(constants.NOTES_LABEL)


class QuoteForm(Form):
    account = StringField(constants.ACCOUNT_LABEL, validators=[DataRequired()])
