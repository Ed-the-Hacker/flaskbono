import click
from flask.cli import with_appcontext

from .extensions import db
from .models import Usuario, Bono

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

def create_data():
    usuario1 = Usuario(1,"daniel", "gerencia")
    bono1 = Bono(1, 20.5, "gerencia")
    usuario2 = Usuario(2,"pedro", "sistemas")
    bono2 = Bono(1, 50, "sistemas")
    db.session.add(usuario1)
    db.session.add(bono1)
    db.session.add(usuario2)
    db.session.add(bono2)
    db.session.commit()