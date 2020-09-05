import os
from flask import Flask, flash, render_template, redirect,request, session,url_for


if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html") 

@app.route('/show_login')  # For the login Button
def show_login():
    return render_template('login.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    users = mongo.db.users
    login_user = users.find_one({'user_username': request.form['user_username']})  #Check if user info is in the system

    if login_user:
        if bcrypt.hashpw(request.form['user_password'].encode('utf-8'), login_user['user_password']) == login_user['user_password']:
            session['user_username'] = request.form['user_username']
            return redirect(url_for('index'))
    else:
        invalid_user = 'Invalid username/password combination'
    return render_template('login.html', message=invalid_user)  # Error message if user info isn't in the system. 


@app.route('/show_register')  # For the register button
def show_register():
    return render_template('register.html')

                         
                     
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)