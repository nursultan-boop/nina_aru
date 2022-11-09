
import os
from flask import Flask, render_template, request, url_for, redirect
import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import sqlalchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:123@localhost:5432/nft_py'
db.init_app(app)
logged_in=False
class nft(db.Model):
    adrs = db.Column(db.String, primary_key=True)
    meta_data = db.Column(db.String, nullable=False)

class Users(db.Model):
    login = db.Column(db.String, primary_key=True)
    pswrd = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()


###
# Routing for your application.
###

@app.route('/', methods=['GET', 'POST'])
def form_example():    
    global logged_in
    if not logged_in:
        return redirect("/login")
    if request.method == 'POST':
        returnValue=""
        address = request.form['address']
        nft_obj = nft.query.filter_by(adrs=address).first()
        if(nft_obj is None):
            url = "https://solana-gateway.moralis.io/nft/mainnet/{}/metadata".format(address)
            headers = {
                "accept": "application/json",
                "X-API-Key": "OjvXHY7ltVwY7xKG1p9HtQmLfKuRiodrazyFMLx2ZAAzECrZY7soe5LMcTTIvj8z"
            }
            returnValue = requests.get(url, headers=headers).text            
            neft = nft(
            adrs=address,
            meta_data=returnValue,
            )
            db.session.add(neft)
            db.session.commit()
            return render_template('meta_data.html', meta_data=returnValue)

    return render_template('nft_styles.html')
    
    # otherwise handle the GET request   

@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in
    logged_in=False
    error = None
    if request.method == 'POST':
        logged_Users = Users.query.filter_by(login=request.form['username']).first()
        logged_pass = Users.query.filter_by(pswrd=str(hash(request.form['password']))).first()
        if logged_Users is None:
            return render_template('sign_in_up.html',login="yes", error='No such User is registered')
        elif logged_pass is None:
            return render_template('sign_in_up.html',login="yes", error='Incorrect password')
        else:
            logged_in=True
            return redirect('/')    
    return render_template('sign_in_up.html',login="yes")

@app.route('/signup', methods=["GET", "POST"])
def Users_create():
    error=None
    logged_in=False
    if request.method == "POST":
        logged_Users = Users.query.filter_by(login=request.form['username']).first()
        if logged_Users is None:
            users = Users(
                login=request.form['username'],
                pswrd=str(hash(request.form['password'])),
            )
            db.session.add(users)
            db.session.commit()
            return redirect('/login')
        else:
            return render_template('sign_in_up.html',error='this User already exists, go to login instead')
    return render_template('sign_in_up.html', login=None)    



if __name__ == '__main__':
    app.run(debug=True)
