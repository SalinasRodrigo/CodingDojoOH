from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Ususario
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("dashboard.html", user = Ususario.get_by_id(session))

@app.route('/logout/process', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

@app.route('/register/process', methods=['POST'])
def registro():
    data = {
        "nombre": request.form['fname'],
        "apellido": request.form['lname'],
        "email": request.form['email'],
        "contraseña": request.form['password'],
        "confirmacion": request.form['confi']
    }
    
    if not Ususario.validacion_registro(data):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data['contraseña'] = pw_hash
    id = Ususario.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login/process', methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    user_in_db = Ususario.get_by_email(data)
    
    if not user_in_db:
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    if len(request.form['password'])<8:
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.contraseña, request.form['password']):
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')