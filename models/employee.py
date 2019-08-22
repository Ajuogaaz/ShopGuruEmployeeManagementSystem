from app import db

class EmployeeModel(db.model):
    __tablename__ = 'employees'

    id = db.column(db.Integer, primary_key=True)
    full_name = db.column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    phone_number = db.Column(db.Integer, nullable=False)
    national_id = db.Column(db.Integer, nullable=False, unique=True)
    kra_pin = db.Column(db.Integer, nullable=False, unique=True)
    salary = db.Column(db.Float, nullable=False)
    benefits = db.Column(db.Float, nullable=False)

