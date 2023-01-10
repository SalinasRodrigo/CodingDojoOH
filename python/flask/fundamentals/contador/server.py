from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta
@app.route('/destroy_session', methods=['POST'])
def create_user():
    print("Got Post Info")
    session.clear()
    return redirect('/contador')
    
@app.route('/contador')
def contador():
    if 'num' in session:
        session['num'] = int(session['num'])+1
    else:
        session['num'] = 0
    return render_template('index.html', num=session['num'])

@app.route('/mas_dos', methods=['POST'])
def mas_dos():
    session['num'] = int(session['num'])+1
    return redirect('/contador')

@app.route('/incremento', methods=['POST'])
def incremento():
    session['num'] = int(session['num'])+int(request.form['incremento'])-1
    return redirect('/contador')

if __name__ == "__main__":
    app.run(debug=True)