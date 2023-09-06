import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///findmenow.db'
    

# For Development Environments
class DevelopmentConfig(Config):
    DEBUG = True

# For Testing Environments
class TestingConfig(Config):
    TESTING = True

# For Production Environments
class ProductionConfig(Config):
    pass  
