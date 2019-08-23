"""This a simulation of a web page server backend for displaying a management system backend data"""
#imports
from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

#custom Imports
from config.configs import Config, DevelopmentConfig,ProductionConfig

"""Instatiate flask as app"""
app = Flask(__name__)

#Import Configs
app.config.from_object(DevelopmentConfig)

#Instatiate SqlAlchemy as db
db = SQLAlchemy(app)

from models.department import DepartmentModel
from models.employee import EmployeeModel

@app.before_first_request
def create_tables():
    db.create_all()



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/departments', methods=['GET','POST'])
def departments():

    all_records = DepartmentModel.fetch_department_records() #Request all current records
    # print(all_records)

    if request.method == 'POST':
        department_name = request.form['departmentname']

        if DepartmentModel.check_department_exist(department_name):
            print('existing record')
        else:
            try:
                department_record = DepartmentModel(name=department_name)
                department_record.create_record()
                print('Successfully added')
                return  redirect(url_for('departments'))

            except Exception as e:
                print("Unable to add record")

    return render_template("departments.html", mydepartments=all_records)

@app.route('/employees', methods=['GET','POST'])
def employees():

    all_records = DepartmentModel.fetch_department_records()
    all_employee_records = EmployeeModel.fetch_employee_records()

    if request.method == 'POST':
        employee_name = request.form['fullName']
        department_name = request.form['department']
        gender_name = request.form['gender']
        email_name = request.form['email']
        phoneNumber_name = request.form['phoneNumber']
        idNumber_name = request.form['idNumber']
        KRApin_name = request.form['KRApin']
        salary_name = request.form['salary']
        benefits_name = request.form['benefits']

        if EmployeeModel.check_employee_exist(idNumber_name):
            print('existing record')
        else:
            try:
                employee_record = EmployeeModel(full_name=employee_name, gender=gender_name, email=email_name, phone_number=phoneNumber_name,
                                                national_id=idNumber_name, kra_pin=KRApin_name, salary=salary_name, benefits=benefits_name,
                                                department_id=department_name)
                employee_record.create_record()
                print('Successfully added')
                return  redirect(url_for('employees'))

            except Exception as e:
                print("Unable to add record")


    return render_template("employees.html", mydepartments=all_records, myemployees=all_employee_records)


if __name__ == '__main__':
    app.run(debug=True)
