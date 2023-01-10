from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')
def level_one():
    return render_template("index.html",num1=8, num2=8, color1='white', color2='black')

@app.route('/<int:num1>')
def one_num(num1):
    return render_template("index.html", num1=num1, num2=8, color1='white', color2='black')

@app.route('/<int:num1>/<int:num2>')
def tow_num(num1, num2):
    return render_template("index.html", num1=num1, num2=num2, color1='white', color2='black')

@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def colors(num1, num2, color1, color2):
    return render_template("index.html", num1=num1, num2=num2, color1=color1, color2=color2)

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)