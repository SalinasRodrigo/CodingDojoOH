from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User


@app.route('/friendships')
def index():
    return render_template("index.html", all_users_friens = User.get_all_user_with_friends(),
                            all_users = User.get_all())


@app.route('/user_process',methods=['POST'])
def create_user():
    data = {
        "fname":request.form['fname'],
        "lname":request.form['lname']
    }
    User.save(data)
    return redirect('/friendships')

@app.route('/friendship_process',methods=['POST'])
def create_book():
    data = {
        "user_id":request.form['user_id'],
        "friend_id":request.form['friend_id']
    }
    User.add_friendship(data)
    return redirect('/friendships')

