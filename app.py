"""This a simulation of a web page server backend for displaying a management system backend data"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

#models
from models.departments import DepartmentModel
from models.employee import EmployeeModel
from config.configs import Config, DevelopmentConfig,ProductionConfig

app.config.from_object('DevelopmentConfig')

@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/departments')
def departments():
    return render_template("departments.html")

@app.route('/employees')
def employees():
    return render_template("employees.html")


if __name__ == '__main__':
    app.run()
