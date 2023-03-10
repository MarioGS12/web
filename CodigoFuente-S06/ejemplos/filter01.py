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

     
    #Like
    vuelos = Flight.query.filter(Flight.origin.like("%a%")).all()

    #IN
    #vuelos = Flight.query.filter(Flight.origin.in_(["Tokyo", "Paris"])).all()

    #AND
    #vuelos = Flight.query.filter(and_(Flight.origin == "Paris",Flight.duration > 500)).all()

    #OR
    #vuelos = Flight.query.filter(or_(Flight.origin == "Paris",Flight.duration > 500)).all()

    #JOIN
    #vuelos = db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()


    for flight in vuelos:
        
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")
        #print(f"{flight.Passenger.name},{flight.Flight.origin} to {flight.Flight.destination}, {flight.Flight.duration} minutes.")




if __name__ == "__main__":
    with app.app_context():
        main()
