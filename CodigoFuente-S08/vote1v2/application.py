import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app, cors_allowed_origins="*")

votes = {"yes": 0, "no": 0, "maybe": 0}
preguntas = []
votos_preguntas = {}
pregunta_actual = ""

@app.route("/")
def index():
    global pregunta_actual
    if pregunta_actual == '':
        return render_template("index.html", votes=votes)
    else:
        return render_template("index.html", votes=votos_preguntas[pregunta_actual], question=pregunta_actual)


@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    question = data["question"]

    if question == '':
        votes[selection] += 1
        emit("vote totals", votes, broadcast=True)
    else:
        # selecciono la pregunta y el voto de esa pregunta y aumento en uno
        votos_preguntas[question][selection] += 1
        # enviar los votos de esa pregunta, y solo a los que esan votando esa pregunta.
        emit("vote totals", votos_preguntas[question],to=question)


@socketio.on("agregar pregunta")
def agregar_pregunta(data):

    pregunta = data["pregunta"]

    # valido que la pregunta no se repita
    if pregunta in preguntas:
        data["error"] = "La Pregunta ya existe."
    else:
        preguntas.append(pregunta)
        # inicializo los votos de esa pregunta
        votos_preguntas[pregunta] = {"yes": 0, "no": 0, "maybe": 0}

    # emito xd
    emit("pregunta nueva", data, broadcast=True)

@socketio.on("cargar preguntas")
def load_questions(data):
    emit("cargar preguntas", {"preguntas": preguntas})

@socketio.on("cargar votos")
def load_votes(data):

    global pregunta_actual
    question = data['pregunta']

    if pregunta_actual != "":
        leave_room(pregunta_actual)

    pregunta_actual = question

    join_room(question)
    emit("cargar votos", votos_preguntas[question], to=question)