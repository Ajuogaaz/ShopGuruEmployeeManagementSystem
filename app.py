"""This a simulation of a web page server backend for displaying a management system backend data"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
