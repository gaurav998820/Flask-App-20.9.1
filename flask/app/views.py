from app import app
from flask import render_template


@app.route( "/home")
def home():
    return ("Hello<h1>Hello World from Flask</h1>")

@app.route( "/<name>")
def namecalling(name):
    return render_template("index.html",content=name)
