from flask_app import db

class User(db.Model):
    __tablename__='User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    birth = db.Column(db.DateTime(), nullable=False)

class Movie(db.Model):
    __tablename__='Movie'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id', ondelete='CASCADE'))
    budget = db.Column(db.Integer, nullable=False)
    runtime = db.Column(db.Integer, nullable=False)
    revenue = db.Column(db.Integer, nullable=False)