from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/play')
def level_one():
    return render_template("index.html",num=3,color="#9fc5f8")

@app.route('/play/<int:num>')
def level_two(num):
    return render_template("index.html", num=num, color="#9fc5f8")

@app.route('/play/<int:num>/<string:color>')
def level_three(num, color):
    return render_template("index.html", num=num, color=color)


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración