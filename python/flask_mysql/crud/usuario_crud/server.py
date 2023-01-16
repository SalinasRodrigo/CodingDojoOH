from flask import Flask, render_template, redirect, request
# importar la clase de friend.py
from usuario import Usuario
app = Flask(__name__)
@app.route('/')
def index():
    ususarios = Usuario.get_all()
    print(ususarios)
    return render_template("index.html", all_users = ususarios)

@app.route('/new_user')
def new():
    return render_template("new_user.html")

@app.route('/update_user/<int:id>')
def update(id):
    user = Usuario.get_by_id(id)
    return render_template("update.html", usuario=user)

@app.route('/show/<int:id>')
def show(id):
    user = Usuario.get_by_id(id)
    return render_template("show.html", usuario=user)

@app.route('/process', methods=["POST"])
def create_user():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    id=Usuario.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/show/%s'%id)

@app.route('/update_user/process/<int:id>', methods=["POST"])
def update_user(id):
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Usuario.update(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/show/%s'%id)

@app.route('/delete_user/process/<int:id>', methods=["POST"])
def delete_user(id):
    Usuario.delete(id)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)