from Flask.app import app
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
        print('in views factorial for number:-', number)
        #factorial_result = factorial.factorial(number)
        print('in view get all cache data', connectionredis.r.hgetall('factorial'))
        factorial_result = connectionredis.factorial_cache(number)
        return render_template("success.html",result=factorial_result,factorial_number=number)
    else:
        number = int(request.args.get('factorial_number'))
        print('in views factorial for number:-', number)
        # factorial_result = factorial.factorial(number)
        print('in view get all cache data', connectionredis.r.hgetall('factorial'))
        factorial_result = connectionredis.factorial_cache(number)
        return render_template("success.html", result=factorial_result, factorial_number=number)
