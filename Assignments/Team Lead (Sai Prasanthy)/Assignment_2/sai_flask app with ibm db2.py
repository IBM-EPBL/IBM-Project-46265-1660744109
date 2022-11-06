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

from flask import Flask
from flask_db2 import DB2

app = Flask(__name__)

app.config['DB2_DATABASE'] = 'sample'
app.config['DB2_HOSTNAME'] = 'localhost'
app.config['DB2_PORT'] = 50000
app.config['DB2_PROTOCOL'] = 'TCPIP'
app.config['DB2_USER'] = 'db2inst1'
app.config['DB2_PASSWORD'] = 'db2inst1'

db = DB2(app) #You forgot that


@app.route('/')
def index():
    cur = db.connection.cursor()
    cur.execute("select id FROM users")
