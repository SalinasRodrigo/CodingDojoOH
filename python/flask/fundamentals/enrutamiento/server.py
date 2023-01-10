from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'hola mundo'

@app.route('/dojo')
def dojo():
    return '¡Dojo!'  


@app.route('/say/<string:name>')
def hola(name):
    print(name)
    return f'¡Hola, {name}!'

@app.route('/repeat/<int:i>/<string:say>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(i, say):
    return f'<p>{say}</p>'*i

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return '<h1>¡Lo siento! No hay respuesta. Inténtalo otra vez.<h1>'

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración