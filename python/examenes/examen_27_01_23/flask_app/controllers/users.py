from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.thought import Thought
from flask_app.models.like import Like


bcrypt = Bcrypt(app)

#Users
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/thoughts')
    return render_template("index.html")

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
    return redirect('/')

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
    return redirect('/thoughts')

@app.route('/logout/process', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

#Toughts ----------------------------------------------------------------------------------------------

@app.route('/thoughts')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("thoughts.html", user_session = User.get_by_id(session),
                            all_thoughts = Thought.get_all_user_thoughts(), all_likes = Like.get_all())

@app.route('/delete/process/<int:id>', methods=['POST'])
def delete_thought(id):
    data = {
        "id": id
    }
    Thought.destroy(data)
    return redirect ('/thoughts')


@app.route('/created/process', methods=['POST'])
def create_thought_process():
    data = {
        "contents": request.form['contents'],
        "user_id": session['user_id']
    }
    if len(data['contents'])<5 or data['contents']=="":
        flash('Thought should be at least 5 characters.', 'thought')
        return redirect ('/thoughts')
    Thought.save(data)
    return redirect ('/thoughts')


@app.route('/user/<int:user_id>')
def view_thoughts_user(user_id):
    data = {
        "user_id": user_id
    }
    return render_template ('user_thoughts.html', user_session = User.get_by_id(session), user_thoughts = User.get_user_thoughts(data) )

#likes----------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/like/<int:user_id>/<int:thought_id>', methods=['POST'])
def like(user_id, thought_id):
    data = {
        "user_id": user_id,
        "thought_id": thought_id
    }
    Like.save(data)
    return redirect ('/thoughts')

@app.route('/un_like/<int:user_id>/<int:thought_id>', methods=['POST'])
def un_like(user_id, thought_id):
    data = {
        "user_id": user_id,
        "thought_id": thought_id
    }
    Like.destroy(data)
    return redirect ('/thoughts')




