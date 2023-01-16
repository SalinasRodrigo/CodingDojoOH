from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/dojos')
def index():
    return render_template("index.html", all_dojos = Dojo.get_all_dojo())

@app.route('/ninjas')
def ninjas():
    return render_template("ninja.html", all_dojos = Dojo.get_all_dojo())

@app.route('/dojo/<int:dojo_id>')
def dojos(dojo_id):
    return render_template("dojo.html", dojo = Dojo.get_dojo_with_ninjas(dojo_id))

@app.route('/dojo/process',methods=['POST'])
def create_dojo():
    data = {
        "name":request.form['name'],
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/ninja/process', methods=['POST'])
def create_ninja():
    data = {
        "fname": request.form['first_name'],
        "lname": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.save(data)
    return  redirect('/dojo/'+data['dojo_id'])
