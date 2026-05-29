from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route("/", methods =['GET'])
def index():
    return render_template('index.html')

@app.route("/notes/web-pentest", methods =['GET'])
def web_pentest():
    return render_template('web-pentest.html')
