
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

	
class Book(db.Model):
	__tablename__="books1"
	isbn= db.Column(db.String, primary_key= True)	
	title= db.Column(db.String, nullable=False)
	author=db.Column(db.String, nullable=False)
	year= db.Column(db.String, nullable=False)
class User(db.Model):
	__tablename__='user'
	id= db.Column(db.String,  primary_key=True)
	name= db.Column(db.String, unique=True)
	password= db.Column(db.String, unique=True)
class Reviews(db.Model):
	__tablename__='reviews'
	id= db.Column(db.String)
	username= db.Column(db.String)
	review= db.Column(db.String, primary_key=True)





