from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Project(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64),index=True)
	description = db.Column(db.String(500))
	date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	time = db.Column(db.Integer)
	state = db.Column(db.String(2))
	user_Id= db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Project {}'.format(self.title)