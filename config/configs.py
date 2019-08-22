class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    debug = True
    SqlAlchemy_database_URI = "postgresql://postgres:Ajuogaaz1753@127.0.0.1:5432/ShopGuruEmployeeManagementDatabase"
    secretKey = "Ajuogaaz"

class ProductionConfig():
    debug = False
