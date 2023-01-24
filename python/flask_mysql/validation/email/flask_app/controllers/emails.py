from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email


@app.route('/email')
def index():
    return render_template("index.html")

@app.route('/success')
def success():
    return render_template("success.html", all_emails=Email.get_all())


@app.route('/email/process',methods=['POST'])
def create_user():
    data = {
        "email":request.form['email']
    }
    if not Email.validacion(data):
        return redirect('/email')
    flash('The email address you entered is a valid email address! Thanks you!')
    Email.save(data)
    return redirect('/success')

@app.route('/delete/process/<int:id>', methods=['POST'])
def delete(id):
    Email.destroy(id)
    return redirect('/success')

