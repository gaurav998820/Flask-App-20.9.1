from Flask.app import application
from flask import render_template


@application.route( "/")
def home():
    return ("Hello<h1>Hello World from Flask</h1>")

@application.route( "/<name>")
def namecalling(name):
    return render_template("index.html",content=name)
