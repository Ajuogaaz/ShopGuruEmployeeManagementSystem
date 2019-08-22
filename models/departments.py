""" This is to create a department table"""
from app import db

class DepartmentModel(db.Model):
    __tablename__ = 'departments' #This is the table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)

    employee = db.relationship('EmployeeModel', backref='department', lazy=True)
