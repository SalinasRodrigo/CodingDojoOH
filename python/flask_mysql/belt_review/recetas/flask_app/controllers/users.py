from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/recipes')
    return render_template("index.html")

@app.route('/recipes')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("recipes.html", user_session = User.get_by_id(session), recipe_user = Recipe.get_all_user_recipes())

@app.route('/recipe/created')
def create_recipe():
    return render_template("created.html")

@app.route('/recipe/update/<int:recipe_id>')
def update_recipe(recipe_id):
    data = {
        "recipe_id": recipe_id
    }
    return render_template("updated.html", recipe = Recipe.get_one_user_recipes(data))

@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    data = {
        "recipe_id": recipe_id
    }
    return render_template ('one_recipe.html', recipe = Recipe.get_one_user_recipes(data) )

@app.route('/logout/process')
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
    return redirect('/recipes')

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
    return redirect('/recipes')

@app.route('/recipe/process', methods=['POST'])
def create_recipe_process():
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "time": request.form['time'],
        "date": request.form['date'],
        "user_id": session['user_id']
    }
    if not Recipe.validation(data):
        return redirect ('/recipe/created')
    id = Recipe.save(data)
    return redirect ('/recipe/'+str(id))

@app.route('/update/process/<int:id>', methods=['POST'])
def update_recipe_process(id):
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "time": request.form['time'],
        "date": request.form['date'],
        "id": id
    }
    if not Recipe.validation(data):
        return redirect ('/update/process/'+str(id))
    Recipe.update(data)
    return redirect ('/recipe/'+str(id))

@app.route('/delete/process/<int:id>')
def delte_recipe(id):
    data = {
        "id": id
    }
    recipe = Recipe.get_one(data)
    if not recipe.user_id == session['user_id']:
        return redirect('/recipes')
    Recipe.destroy(data)
    return redirect ('/recipes')