
import os
from flask import Flask, render_template, request, url_for, redirect
import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import sqlalchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://qanbbuderamayy:0629f6743d9670208524b1e55754dfaa7ee6f5a03b3970ec0a207034430ec992@ec2-34-247-72-29.eu-west-1.compute.amazonaws.com:5432/d69ut5v5lplk9d'
db.init_app(app)
logged_in=False
class nft_info(db.Model):
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
        if logged_in==False:
            return redirect('/login') 
        returnValue=""
        address = request.form['address']
        nft_obj = nft_info.query.filter_by(adrs=address).first()
        if(nft_obj is None):
            url = "https://solana-gateway.moralis.io/nft/mainnet/{}/metadata".format(address)
            headers = {
                "accept": "application/json",
                "X-API-Key": "OjvXHY7ltVwY7xKG1p9HtQmLfKuRiodrazyFMLx2ZAAzECrZY7soe5LMcTTIvj8z"
            }
            returnValue = requests.get(url, headers=headers).text            
            neft = nft_info(
            adrs=address,
            meta_data=returnValue,
            )
            db.session.add(neft)
            db.session.commit()
            return render_template('meta_data.html', meta_data=returnValue)

    return render_template('nft.html')
    
    # otherwise handle the GET request   

@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in
    error = None
    if request.method == 'POST':
        user_login = Users.query.filter_by(login=request.form['username']).first()
        user_pass = Users.query.filter_by(pswrd=str(hash(request.form['password']))).first()
        if user_login is None:
            return render_template('login_page.html', error='Need to register')
        elif user_pass is None:
            return render_template('login_page.html', error='Wrong password')
        else:
            logged_in=True
            return redirect('/')    
    return render_template('login_page.html')

@app.route('/reg', methods=["GET", "POST"])
def Users_create():
    error=None
    if request.method == "POST":
        user_login = Users.query.filter_by(login=request.form['username']).first()
        if user_login is None:
            users = Users(
                login=request.form['username'],
                pswrd=str(hash(request.form['password'])),
            )
            db.session.add(users)
            db.session.commit()
            return redirect('/login')
        else:
            return render_template('reg.html',error='User already registered')
    return render_template('reg.html')   



if __name__ == '__main__':
    app.run(debug=True)
