from  app import db

class DepartmentModel(db.Model):
    __tablename__ = 'departments' #This is the table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    employee = db.relationship('EmployeeModel', backref='department', lazy=True)

    def create_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def check_department_exist(cls, name):
        records = DepartmentModel.query.filter_by(name=name).first()

        if records:
            return True
        else:
           return False

    @classmethod
    def fetch_department_records(cls):
        return DepartmentModel.query.all()
