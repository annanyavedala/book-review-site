import os

from flask import Flask, session, render_template, request,flash, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.config["SQLALCHEMY_DATABASE_URI"]= os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
db= SQLAlchemy()

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login", methods=["GET"])
def login():
	return render_template("login.html")
@app.route("/", methods=["POST"])
def check_user():
	username= request.form.get('id2')
	name= request.form.get('name2')
	password= request.form.get('password2')
	username1= User.query.filter_by(id=username).first()
	name1= User.query.filter_by(name=name).first()
	password1= User.query.filter_by(password=password).first()
	if not username1 or not name1 or not password1:
		return render_template("search.html")
	else:
		return redirect(url_for("login"))

	
	
@app.route("/register", methods=["GET"])
def register():
		return render_template("register.html")

@app.route("/add_user", methods=['POST'])
def add_user():
	
	username = request.form.get('id1')
	name = request.form.get('name1')
	password = request.form.get('password1')
	user= User.query.filter_by(id=username).first()
	if user:
		return render_template("register.html")
	else:
		new_user= User(id=username, name=name, password=password)
		db.session.add(new_user)
		db.session.commit()
		return redirect(url_for("login"))

@app.route("/search", methods=['GET'])
def search1():
	return render_template("search.html")

@app.route("/show", methods=['POST'])
def show():
	m= request.form.get("details")
	details1= Book.query.filter_by(title=m).all()
	details2= Book.query.filter_by(isbn=m).all()
	details3= Book.query.filter_by(author=m).all()
	details4= Book.query.filter_by(year=m).all()
	if details1:
		return render_template("show.html", details=details1)
	if details2:
		return render_template("show.html", details=details2)
	if details3:
		return render_template("show.html", details=details3)
	if details4:
		return render_template("show.html", details=details4)
	else:
		flash("Enter valid data")
@app.route("/final", methods=['POST'])
def final():
		p= request.form.get("final")
		q= request.form.get("check_username")
		check = Reviews.query.filter(and_(Reviews.id==p, Reviews.username==q)).count()
		s=Book.query.filter_by(isbn=p).first()
		reviews_f= Reviews.query.filter_by(id=p)
		if check:
			return render_template("review.html", s=s, q=q, reviews_f=reviews_f)
		else:
			return render_template("final.html", s=s, q=q, reviews_f=reviews_f)

@app.route("/temp", methods=['POST', 'GET'])
def temp():
	if request.method=='POST':
		q = request.form.get("username")
		p = request.form.get("isbn")
		s=Book.query.filter_by(isbn=p).first()
		reviews = request.form.get("review")
		review1= Reviews(id=p, username=q, review=reviews)
		db.session.add(review1)
		db.session.commit()
	reviews_f= Reviews.query.filter_by(id=p)
	return render_template("review.html", s=s, q=q, reviews_f=reviews_f)


	

# @app.route("/final", methods=['POST'])
# def final1():
# 	p= request.form.get("final")
# 	finals=Book.query.filter_by(isbn=p).first()
# 	q= request.form.get("check_username")
# 	reviews= request.form.get("review")
# 	check = Reviews.query.filter(and_(Reviews.id==p, Reviews.username==q)).count()
# 	if check:
# 		flash("You cannot post a review")
# 		return render_template("final.html")
# 	else:
# 		review1= Reviews(id=p, username=q, review=reviews)
# 		db.session.add(review1)
# 		db.session.commit()
# 	reviews_f= Reviews.query.all()
# 	return render_template("final.html" , reviews_f=reviews_f, p=finals)
@app.route("/main1")
def main1():
    return render_template("main.html")
		
