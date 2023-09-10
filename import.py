import os
import csv

from flask import Flask, render_template, request
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


db.init_app(app)

def main():
	with open("books1.csv", "r", ) as xyz:
		reader1= csv.reader(xyz)
		for isbn,title,author, year in reader1:
			book= Book(isbn=isbn, title=title, author=author, year=year)
			db.session.add(book)
			continue
	db.session.commit()

if(__name__)=="__main__":
	with app.app_context():
		main()
