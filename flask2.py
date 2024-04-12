
from flask import Flask, render_template, request
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

with open('config.json', 'r') as c:
    params=json.load(c)
    
    
local_server= True
app = Flask(__name__)

# Update the database configuration to use 'mysql-connector-python'
if params["local_server"]=='True':
    app.config['SQLALCHEMY_DATABASE_URI'] = params.get("local_uri")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params.get('prod_uri')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
db = SQLAlchemy(app)

# Rest of your code
class contacts(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    serial = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_no = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

@app.route("/")
def home():
    return render_template('index.html',params=params)


@app.route("/about")
def about():
    return render_template('about.html',params=params)


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = contacts(name=name, phone_no = phone, message = message,date= datetime.now(), email = email )
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html',params=params)


app.run(debug=True)



