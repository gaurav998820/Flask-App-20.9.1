from app import app
from flask import render_template,request,redirect
from Flask.app import factorial
from Flask.app import connectionredis


#@app.route( "/home")
#def home():
#    return ("Hello<h1>Hello World from Flask</h1>")

#@app.route( "/<name>")
#def namecalling(name):
#    return render_template("index.html",content=name)

@app.route( "/")
def welcomepage():
    connectionredis.factorial_flush()
    return render_template("welcomepage.html")

@app.route( "/success", methods=['POST','GET'])
def success():
    if request.method == 'POST':
        number = int(request.form['factorial_number'])
        print('in views factorial for number:', number)
        print('in view get all cache data',)
    return render_template("index.html",content=name)
