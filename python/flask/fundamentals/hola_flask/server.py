from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/success')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def success():
    return 'success'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'hola mundo'

@app.route('/hola/<name>')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola(name):
    print(name)
    return "Hola, " + name

@app.route('/users/<username>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración