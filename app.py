"""This a simulation of a web page server backend for displaying a management system backend data"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

"""Instatiate flask as app"""
app = Flask(__name__)

"""Instatiate SqlAlchemy as db"""
db = SQLAlchemy(app)


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
    app.run(debug=True)
