from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import text
import re
from database import engine

app = Flask(__name__)
start = True  #game status update to start

app.secret_key = 'ctfkimaakabhosada'


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
  msg = ''
  if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    username = request.form['username']
    password = request.form['password']
    query = text(
        'SELECT * FROM accounts WHERE username = :username AND password = :password'
    )

    # Define a dictionary of parameters to substitute into the query
    params = {"username": username, "password": password}

    # Execute the query with the parameters
    result = engine.connect().execute(query, params)
    account = result.fetchone()
    if account:
      session['loggedin'] = True
      session['id'] = int(account[0])
      session['username'] = account[1]
      msg = 'Logged in successfully !'
      if(start):
        return render_template('game.html', msg=msg)
      else:
        return render_template('nogame.html', msg=msg)
    else:
      msg = 'Incorrect username / password !'
  return render_template('login.html', msg=msg)


# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('id', None)
#     session.pop('username', None)
#     return redirect(url_for('login'))

# @app.route('/register', methods =['GET', 'POST'])
# def register():
#     msg = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
#         account = cursor.fetchone()
#         if account:
#             msg = 'Account already exists !'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             msg = 'Invalid email address !'
#         elif not re.match(r'[A-Za-z0-9]+', username):
#             msg = 'Username must contain only characters and numbers !'
#         elif not username or not password or not email:
#             msg = 'Please fill out the form !'
#         else:
#             cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
#             mysql.connection.commit()
#             msg = 'You have successfully registered !'
#     elif request.method == 'POST':
#         msg = 'Please fill out the form !'
#     return render_template('register.html', msg = msg)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
