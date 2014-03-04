class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    import os
    db_path = os.path.join(os.getcwd(), 'production.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
    SECRET_KEY = 'Change before going live!'
