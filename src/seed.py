from models import db, User, Planet, People
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    print("🚀 Poblando la base de datos...")
    db.drop_all()
    db.create_all()

    # Usuarios
    user1 = User(email="luke@jedi.com", password="123", is_active=True, first_name="Luke", last_name="Skywalker")
    user2 = User(email="leia@rebels.com", password="456", is_active=True, first_name="Leia", last_name="Organa")

    # Planetas
    planet1 = Planet(name="Tatooine", climate="Arid", population="200000")
    planet2 = Planet(name="Naboo", climate="Temperate", population="4500000")

    # Personajes
    people1 = People(name="Luke Skywalker", gender="Male", height="172")
    people2 = People(name="Leia Organa", gender="Female", height="150")

    db.session.add_all([user1, user2, planet1, planet2, people1, people2])
    db.session.commit()

    print("✅ Datos insertados correctamente.")
