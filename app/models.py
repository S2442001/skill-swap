from flask_sqlalchemy import SQLAlchemy 
from app.extensions import db
from flask_login import UserMixin


#association table between user and skill
user_skills=db.Table(
    "user_skills",

    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("skill_id", db.Integer, db.ForeignKey("skill.id"), primary_key=True),
    db.Column("type", db.String(100), nullable=False) #offered or requested
)

class User(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100), nullable=False, unique=True)
    email=db.Column(db.String(100), nullable=False, unique=True)
    password_hash=db.Column(db.String(500), nullable=False)

    skills=db.relationship("Skill", secondary=user_skills, backref="users")


class Skill(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

 