from flask import Flask, flash, render_template, request, redirect, session
from dojo import Dojo


app = Flask(__name__)
app.secret_key="ke onda ke pex"

@app.route('/result/<int:id>')
def resultados(id):
    return render_template('resultados.html', dojo=Dojo.get_by_id(id))

@app.route('/encuesta')
def encuesta():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def procesar():

    data = {
        "name": request.form['name'],
        "idioma": request.form['idioma'],
        "ubicacion": request.form['ubicacion'],
        "comentario": request.form['comentario']    
    }
    print(request.form['name'],  request.form['idioma'], request.form['ubicacion'], request.form['comentario'])
    if not Dojo.validation(data):
        return redirect('/encuesta')
    id = Dojo.save(data)
    return redirect('/result/'+str(id))

if __name__ == "__main__":
    app.run(debug=True)