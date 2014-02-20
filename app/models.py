import constants
from flask.ext.sqlalchemy import orm, SQLAlchemy

db = SQLAlchemy()


class Engagement(db.Model):
    __tablename__ = 'engagement'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(*constants.ENGAGEMENT_TYPES), nullable=False)
    renewal = db.Column(db.Boolean)
    number_of_reports = db.Column(db.Integer,
                                  default=constants.NUMBER_OF_REPORTS)
    amount_of_retesting = db.Column(db.Integer,
                                    default=constants.RETESTING_HOURS)

    # Constraints
    reporting_frequency = db.Column(db.Enum(*constants.REPORTING))

    time_window = db.Column(db.String, default=None)
    deadline = db.Column(db.Date)
    security_appliances = db.Column(db.Enum(*constants.APPLIANCES))
    permit_whitelisting = db.Column(db.Boolean)
    bandwidth_restrictions = db.Column(db.String)
    uses_third_parties = db.Column(db.Boolean)
    third_parties = db.Column(db.String)
    past_issues = db.Column(db.Boolean)
    notes = db.Column(db.Text)

    # Relationships
    services = orm.relationship('Service')

    def __init__(self, **kwargs):
        for (k, v) in kwargs.items():
            if k in Engagement.__dict__:
                if k[0] != '_' or k != 'id':
                    setattr(self, k, v)


class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))

    # Constraints
    environment = db.Column(db.Enum(*constants.ENVIRONMENT))

    time_window = db.Column(db.String)
    deadline = db.Column(db.Date)
    security_appliances = db.Column(db.Enum(*constants.APPLIANCES))
    permit_whitelisting = db.Column(db.Boolean)
    bandwidth_restrictions = db.Column(db.String)
    uses_third_parties = db.Column(db.Boolean)
    third_parties = db.Column(db.String)
    past_issues = db.Column(db.Boolean)
    notes = db.Column(db.Text)

    # Relationships
    engagement_id = db.Column(db.Integer, db.ForeignKey('engagement.id'))

    # Polymorphism
    __mapper_args__ = {
        'polymorphic_identity': 'service',
        'polymorphic_on': type,
        'with_polymorphic':  '*'
    }

    def __init__(self, **kwargs):
        for (k, v) in kwargs.items():
            if k in Service.__dict__:
                if k[0] != '_' or k != 'id':
                    setattr(self, k, v)


class Application(Service):
    __tablename__ = 'application'
    id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)
    link = db.Column(db.String)
    non_auth_assessment = db.Column(db.Boolean)
    requires_auth = db.Column(db.Boolean)
    role_count = db.Column(db.Integer)
    roles = db.Column(db.String)
    public_registration = db.Column(db.Boolean)
    size = db.Column(db.Enum(*constants.SIZE_OF_APPLICATION))

    # Constraints
    blacklisted_pages = db.Column(db.Text)
    requires_two_factor = db.Column(db.Boolean)
    two_factor_methods = db.Column(db.Enum(*constants.TWO_FACTOR_METHODS))
    live_database = db.Column(db.Boolean)

    # Polymorphism
    __mapper_args__ = {
        'polymorphic_identity': 'application',
    }

    def __init__(self, **kwargs):
        for (k, v) in kwargs.items():
            if k in Application.__dict__:
                if k[0] != '_' or k != 'id':
                    setattr(self, k, v)


class API(Service):
    __tablename__ = 'api'
    id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)
    link = db.Column(db.String)
    non_auth_assessment = db.Column(db.Boolean)
    requires_auth = db.Column(db.Boolean)
    role_count = db.Column(db.Integer)
    roles = db.Column(db.String)
    public_registration = db.Column(db.Boolean)
    size = db.Column(db.Enum(*constants.SIZE_OF_APPLICATION))
    documentation = db.Column(db.Boolean)
    documentation_quality = db.Column(db.Enum(*constants.DOCUMENTATION_QUALITY))
    message_format = db.Column(db.Enum(*constants.MESSAGE_FORMAT))
    prepopulated_objects = db.Column(db.Boolean)
    test_suites_available = db.Column(db.Boolean)

    # Constraints
    os_specific = db.Column(db.Boolean)
    requires_installation = db.Column(db.Boolean)
    hardware_requirement = db.Column(db.Boolean)
    HMAC_required = db.Column(db.Boolean)
    blacklisted_pages = db.Column(db.Text)
    requires_two_factor = db.Column(db.Boolean)
    two_factor_methods = db.Column(db.Enum(*constants.TWO_FACTOR_METHODS))
    live_database = db.Column(db.Boolean)

    # Polymorphism
    __mapper_args__ = {
        'polymorphic_identity': 'api',
    }

    def __init__(self, **kwargs):
        for (k, v) in kwargs.items():
            if k in API.__dict__:
                if k[0] != '_' or k != 'id':
                    setattr(self, k, v)


class NetworkLayer(Service):
    __tablename__ = 'network'
    id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)
    scope = db.Column(db.Text)
    unique_services = db.Column(db.Integer)

    # Polymorphism
    __mapper_args__ = {
        'polymorphic_identity': 'network',
    }

    def __init__(self, **kwargs):
        for (k, v) in kwargs.items():
            if k in Network.__dict__:
                if k[0] != '_' or k != 'id':
                    setattr(self, k, v)


class Perspective(Service):
    __tablename__ = 'perspective'
    id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)
    name = db.Column(db.String)
    scope = db.Column(db.Text)
    unique_services = db.Column(db.Integer)
    hardware = db.Column(db.Enum(*constants.HARDWARE))

    # Constraints
    single_proxy_multiple_lans = db.Column(db.Boolean)

    # Polymorphism
    __mapper_args__ = {
        'polymorphic_identity': 'perspective',
    }

    def __init__(self, **kwargs):
        for (k, v) in kwargs.items():
            if k in Network.__dict__:
                if k[0] != '_' or k != 'id':
                    setattr(self, k, v)


def query_to_list(query, include_field_names=True):
    """Turns a SQLAlchemy query into a list of data values."""
    column_names = []
    for i, obj in enumerate(query.all()):
        if i == 0:
            column_names = [c.name for c in obj.__table__.columns]
            if include_field_names:
                yield column_names
        yield obj_to_list(obj, column_names)


def obj_to_list(sa_obj, field_order):
    """Takes a SQLAlchemy object - returns a list of all its data"""
    return [getattr(sa_obj, field_name, None) for field_name in field_order]
