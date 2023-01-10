from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key="ke onda ke pex"
@app.route('/result')
def resultados():
    return render_template('resultados.html', name=session['name'], location=session['location'], 
                            language=session['language'], coment=session['coment'])

@app.route('/encuesta')
def encuesta():
    session.clear()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def procesar():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['coment']=request.form['coment']
    return redirect('/result')

if __name__ == "__main__":
    app.run(debug=True)