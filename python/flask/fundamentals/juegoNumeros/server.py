from flask import Flask, render_template, request, redirect, session
import random 	                # import the random module

app = Flask(__name__)
app.secret_key="ke onda ke pex"
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta
@app.route('/gess', methods=['POST'])
def create_user():
    print("Got Post Info")
    if request.form['gess'] == '':
        return redirect('/juego')
    
    session['intentos']=int( session['intentos'])+1
    
    aux=int(request.form['gess'])

    if  aux == int(session['num']):
        session['correcto']=0
    elif aux < int(session['num']):
        session['correcto']=1
    else:
        session['correcto']=2

    return redirect('/juego')
    
@app.route('/juego')
def contador():
    if 'num' not in session:
        session['num'] = random.randint(1, 100) # random number between 1-100
    if 'correcto' not in session:
        session['correcto'] = -1 # random number between 1-100
    if 'intentos' not in session:
        session['intentos'] = 0 # random number between 1-100

    return render_template('index.html', num=session['num'], correcto=session['correcto'], intentos=session['intentos'])

@app.route('/reset', methods=['POST'])
def reset():
    print("Got Post Info")
    session.pop('num')
    session.pop('intentos')
    session.pop('correcto')
    return redirect('/juego')


if __name__ == "__main__":
    app.run(debug=True)