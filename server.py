from collections import defaultdict, Counter
import json

from flask import Flask, render_template, session
from flask_socketio import SocketIO, send, emit

from problems import problems
from simulation import single_step
from functions import convert

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


def sendj(typ, j):
    send({"type":typ, "data":j}, json=True)

@socketio.on('connect')
def handle_connect():
    print('connected')
    sendj("problems", problems)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send("helo")

records = defaultdict(list)

@socketio.on('json')
def handle_json(j):
    print('received json: ' + str(j))
    if j["type"] == "problem":
        session["sproblem"] = problems[j["data"]]
        session["problem"] = convert(session["sproblem"])
        session["env"] = {}
        session["history"] = []
        sendj("problem", session["sproblem"])
        sendj("env", session["env"])
        sendj("history", session["history"])

    elif j["type"] == "decision":
        session["env"], session["history"] = single_step(session["problem"], session["env"], session["history"], j["data"])
        sendj("env", session["env"])
        sendj("history", session["history"])
        if session["env"]["step"] == session["problem"]["steps"]:
            problemkey = json.dumps(session["sproblem"])
            records[problemkey].append([session["env"], session["history"]])

            c = Counter()

            for record in records[problemkey]:
                c[record[0]["score"]] += 1

            sendj("records", sorted(c.items(), key=lambda item:item[0], reverse=True))

    elif j["type"] == "continue":
        sendj("problems", problems)

if __name__ == '__main__':
    socketio.run(app)
