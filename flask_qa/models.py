from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from .extensions import db 

class Usuario(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    departamento=db.Column(db.String(50))

class Bono(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    cantidad=db.Column(db.DECIMAL(10,2))
    departamento=db.Column(db.String(50))
    