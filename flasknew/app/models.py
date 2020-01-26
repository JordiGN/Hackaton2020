from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from datetime import datetime
from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    projects = db.relationship('Project', backref='author', lazy='dynamic')
    password_hash = db.Column(db.String(128))

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
       self.password_hash = generate_password_hash(password) 

    def __repr__(self):
        return '<User {}>'.format(self.username)  
 

class Project(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64),index=True)
	description = db.Column(db.String(500))
	date = db.Column(db.Integer)
	time = db.Column(db.Integer)
	state = db.Column(db.String(2))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    #users = db.relationship(User)

	def __repr__(self):
		return '<Project {}'.format(self.title)

# import sqlite3


# class Schema:
#     def __init__(self):
#         self.conn = sqlite3.connect('hackaton.db')
#         self.create_user_table()
#         #self.createProject()
#         self.curs = self.conn.cursor()
#         # Why are we calling user table before to_do table
#         # what happens if we swap them?

#     def create_to_do_table(self):

#         query = """
#         CREATE TABLE IF NOT EXISTS "Todo" stuffToPlot(
#             userId INTEGER,
#             first_name TEXT, 
#             last_name TEXT, 
#             email TEXT,
#             street_address TEXT, 
#             city TEXT, 
#             state TEXT, 
#             task TEXT, 
#             description TEXT, 
#             date TEXT
#         );
#         """

#         self.conn.execute(query)

#     def create_user_table(self):
#         query = """
#         CREATE TABLE IF NOT EXISTS "Users" stuffToPlot(
#          userId INTEGER PRIMARY KEY,
#          name TEXT,
#          email VARCHAR(320),
#          psswd TEXT
#         );
#         """
#         self.conn.execute(query)
#         # create user table in similar fashion
#         # come on give it a try it's okay if you make mistakes

# class UserModel:
#     #TABLENAME = "Users"

#     def __init__(self):
#         self.conn = sqlite3.connect('hackaton.db')
#         self.curs = self.conn.cursor()
#         self.TABLENAME = "Users"

#     def create(self, userId, name, email, psswd):
#         query = f'insert into {self.TABLENAME} ' \
#                 f'(userId, name, email, psswd) ' \
#                 f'values ("{userId}","{name}","{email}","{psswd}")'
#         result = self.curs.execute(query)
#         return result
#    # Similarly add functions to select, delete and update todo

# class TodoModel:
#     #TABLENAME = "Todo"

#     def __init__(self):
#         self.conn = sqlite.connect('hackathon.db')
#         self.curs = self.conn.cursor()
#         self.TABLENAME = "Todo"

#     def sqlSelect(self, state):
#         st = (state,)
#         newTable = self.curs.execute("SELECT * FROM {TABLENAME} WHERE state = ?", st)
#         return newTable
