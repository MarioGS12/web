import os

from flask import render_template, Flask
from flask_socketio import SocketIO, emit, join_room, leave_room
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app, cors_allowed_origins="*")



@app.route("/", methods=["post","get"])
def index():
    return render_template("inicio.html")

@app.route("/room", methods=["post","get"])
def sala():
    return render_template("room.html")


@socketio.on("general")
def general(data):
    chat = data["chat"]
    sala = data["room"]
    leave_room(sala)
    emit("general respuesta", {"chat":chat}, broadcast=True)


@socketio.on("sala01")
def room(data):
    chat = data["chat"]
    sala = data["room"]
    print(chat)
    join_room(sala)
    emit("sala01 respuesta", {"chat":chat}, to=sala)