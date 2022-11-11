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
