from flask import Flask, render_template, request, redirect
from datetime import datetime
import calendar
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    date = [calendar.month_name[datetime.now().month], datetime.now().day, datetime.now().year, datetime.now().hour, datetime.now().minute, datetime.now().second]
    num = int(request.form['apple'])+int(request.form['raspberry'])+int(request.form['strawberry'])
    print('Cobrando a '+request.form['first_name']+f' por {num} frutas')
    return render_template("checkout.html", request=request.form, num=num, date=date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    