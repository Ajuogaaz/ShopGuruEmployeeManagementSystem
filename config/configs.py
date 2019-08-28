class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Ajuogaaz1753@127.0.0.1:5432/ShopGuruEmployeeManagementDatabase"
    SECRET_KEY = "Ajuogaaz"

class ProductionConfig():
    DEBUG = False
