import ibm_db
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT= 30376;SECURITY=SSL;ServerCertificate= DigiCertGlobalRootCA (1).crt;UID= kbb44821;PWD=wdJPZiqUY9AlChkx",")
from flask import Flask;
from flask import render_template;

app = Flask(_name_)

@app.route("/")
@app.route("/home")
def home():
return render_template('home.html')

@app.route("/index")
def index():
return render_template('index.html')

@app.route("/about")
def about():
return render_template('about.html')

@app.route("/signup")
def signup():
return render_template('signup.html')
  
if_name_=='_main_':
app.run(debug=True)
