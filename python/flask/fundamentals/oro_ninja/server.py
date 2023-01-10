from flask import Flask, render_template, request, redirect, session
import random 	                # import the random module
from datetime import datetime
app = Flask(__name__)
app.secret_key="ke onda ke pex"
@app.route('/')
def oro():
    if 'oro' not in session:
        session['oro']=0
    if 'lineas' not in session:
        session['lineas']=[]
    return render_template('index.html', oro=session['oro'], lineas=session['lineas'])

@app.route('/process', methods=['POST'])
def procesar():
    flag=0
    if request.form['which_form']=='farm':
        oro_ganado=random.randint(10, 20)
        session['oro']=int(session['oro'])+oro_ganado
    if request.form['which_form']=='cave':
        oro_ganado=random.randint(5, 10)
        session['oro']=int(session['oro'])+oro_ganado
    if request.form['which_form']=='house':
        oro_ganado=random.randint(2, 5)
        session['oro']=int(session['oro'])+oro_ganado
    if request.form['which_form']=='casino':
        flag=random.randint(0, 1)
        if flag==0:
            oro_ganado=random.randint(0, 50)
            session['oro']=int(session['oro'])+oro_ganado
        elif flag==1:
            oro_ganado=random.randint(0, 50)
            session['oro']=int(session['oro'])-oro_ganado
    lugar=request.form['which_form']
    f=datetime.now()
    if flag==0:
        new_line=f'<p class="text-success">Earned {oro_ganado} golds from the {lugar} ({f.year}/{f.month}/{f.day} {f.strftime("%I")}:{f.strftime("%M")} {f.strftime("%p")})</p>'
    else:
        new_line=f'<p class="text-danger">Earned {oro_ganado} golds from the {lugar} ({f.year}/{f.month}/{f.day} {f.strftime("%I")}:{f.strftime("%M")} {f.strftime("%p")})</p>'
    session['lineas'].insert(0,new_line)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    print("Got Post Info")
    session.pop('oro')
    session.pop('lineas')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)