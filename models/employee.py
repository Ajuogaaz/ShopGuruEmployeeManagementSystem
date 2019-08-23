from app import db

class EmployeeModel(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    phone_number = db.Column(db.Integer, nullable=False)
    national_id = db.Column(db.Integer, nullable=False, unique=True)
    kra_pin = db.Column(db.String(), nullable=False, unique=True)
    salary = db.Column(db.Float, nullable=False)
    benefits = db.Column(db.Float, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

    def create_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def check_employee_exist(cls, Idnumber):
        records = EmployeeModel.query.filter_by(national_id=Idnumber).first()

        if records:
            return True
        else:
            return False

    @classmethod
    def fetch_employee_records(cls):
        return EmployeeModel.query.all()

    @classmethod
    def fetch_by_id(cls, id):
        """Search the specific id"""
        return cls.query.filter_by(id=id).first()
    
