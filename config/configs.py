class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Ajuogaaz1753@127.0.0.1:5432/ShopGuruEmployeeManagementDatabase"
    SECRET_KEY = "Ajuogaaz"

class ProductionConfig():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgres://uzchnigejqqloo:edbfa3115008ffc6d5727cac963b6ea2cd2a2a43027433048f2d75d2acd6705d@ec2-50-17-231-192.compute-1.amazonaws.com:5432/d7i5ajf7jlndhp"
    SECRET_KEY = "Ajuogaaz1753+"
