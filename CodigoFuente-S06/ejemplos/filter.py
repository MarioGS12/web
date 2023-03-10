import os

from flask import Flask, render_template, request
from models import *
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():


    
    

    vuelos = Flight.query.filter(Flight.origin != "Paris").all()
    #vuelos=Flight.query.filter_by(origin != "Paris").all()

    for flight in vuelos:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")




if __name__ == "__main__":
    with app.app_context():
        main()
