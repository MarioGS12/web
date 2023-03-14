import os

from flask import Flask, render_template, request
from sqlalchemy import and_, or_
from models import *
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    #JOIN
    #vuelos = db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()


    #JOIN version sin relationship
    #vuelos = db.session.query(Flight, Passenger).filter(and_(Flight.id == Passenger.flight_id,Passenger.name=="Mario")).first()


    #JOIN version con relationship v1

    #pasajeros= Passenger.query.filter_by(name="Mario")
    #vuelos = pasajeros.first().flight


    #JOIN version con relationship v2

    vuelos = Passenger.query.filter_by(name="Mario").first().flight




    #print(f"{vuelos.Passenger.name},{vuelos.Flight.origin} to {vuelos.Flight.destination}, {vuelos.Flight.duration} minutes.")


    #JOIN version con relationship
    print(f"{vuelos.origin} to {vuelos.destination}, {vuelos.duration} minutes.")

    #for flight in pasajeros:
    #    print(flight.name)


if __name__ == "__main__":
    with app.app_context():
        main()
