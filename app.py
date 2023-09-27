from flask import Flask,render_template

app = Flask(__name__)
global start=False
@app.route("/")#login is default route
def login_render():
  return render_template('login.html')






if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
  