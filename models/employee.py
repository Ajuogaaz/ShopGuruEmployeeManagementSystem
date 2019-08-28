from main import db

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
         return cls.query.filter_by(id=id).first()

    @classmethod
    def update_by_id(cls, id=id, full_name = None,gender = None,kra_pin = None, phone_number = None, email = None,national_id = None,
                     department_id = None,salary = None,benefits = None):

        record = cls.fetch_by_id(id=id)

        if record:
            if full_name:
                record.full_name = full_name
            if gender:
                record.gender = gender
            if kra_pin:
                record.kra_pin = kra_pin
            if phone_number:
                record.phone_number = phone_number
            if email:
                record.email = email
            if national_id:
                record.national_id = national_id
            if department_id:
                record.department_id = department_id
            if salary:
                record.salary = salary
            if record.benefits:
                record.benefits = benefits


            db.session.commit()
            return True

    @classmethod
    def deleteEmployee(cls, id):
        record = cls.query.filter_by(id=id)
        if record.first():
            record.delete()
            db.session.commit()
            return True
        else:
            return False
