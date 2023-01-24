from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.message import Message


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("dashboard.html", user_session = User.get_by_id(session), all_users = User.get_all(),
                            messages = Message.get_by_destinatary(session), num_messages = Message.get_num_messages(session),
                            num_send = Message.get_num_send(session))

@app.route('/logout/process', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

@app.route('/register/process', methods=['POST'])
def registro():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
        "password": request.form['password'],
        "confi": request.form['confi']
    }
    
    if not User.validacion_registro(data):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data['password'] = pw_hash
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login/process', methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    user_in_db = User.get_by_email(data)
    
    if not user_in_db:
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    if len(request.form['password'])<8:
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/message/process/<int:destinatary_id>/<int:remitent_id>', methods=['POST'])
def message(destinatary_id, remitent_id):
    data = {
        "message": request.form['message'],
        "destinatary_id": destinatary_id,
        "remitent_id": remitent_id
    }
    
    if len(request.form['message'])<5:
        flash('La longitud minima del mensaje es de 5 caracteres.', 'message')
        return redirect('/dashboard')
    Message.save(data)
    return redirect('/dashboard')

@app.route('/delete/process/<int:message_id>', methods=['POST'])
def delete_message(message_id):
    Message.destroy(message_id)
    return redirect('/dashboard')