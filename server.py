from collections import defaultdict, Counter
from copy import deepcopy
import json
from time import time

from flask import Flask, render_template, session
from flask_socketio import SocketIO, send, emit

from problems import problems
from simulation import single_step, check_options
from database import get_problemkey

RECORDFILE = "records.txt"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


def sendj(typ, j):
    send({"type":typ, "data":j}, json=True)

@socketio.on('connect')
def handle_connect():
    print('connected')
    sendj("problems", problems)
    sendj("stats", stats())

def stats():
    global totalgames, totalclicks
    return {"totalgames":totalgames, "totalclicks":totalclicks}

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send("helo")

records = defaultdict(list)

@socketio.on('json')
def handle_json(j):
    global records, totalgames, totalclicks
    print('received json: ' + str(j))
    if j["type"] == "problem":
        session["problem"] = problems[j["data"]]
        session["env"] = deepcopy(session["problem"].get("start", {}))
        session["env"]["step"] = 0
        session["env"]["score"] = eval(session["problem"]["score"], session["env"])
        session["history"] = []
        sendj("problem", session["problem"])
        options = check_options(session["problem"], session["env"])
        sendj("options", options)
        if "__builtins__" in session["env"]:
            del session["env"]["__builtins__"]
        sendj("env", session["env"])

    elif j["type"] == "decision":

        if session["env"] is None:
            return

        # TODO avoid double submits somehow
        session["env"], session["history"] = single_step(session["problem"], session["env"], session["history"], j["data"])

        if session["env"]["step"] == session["problem"]["steps"]:

            endtime = time()

            with open(RECORDFILE, "a") as recordfile:
                recordfile.write(json.dumps([session["problem"], session["env"], session["history"], endtime])+"\n")

            totalgames += 1
            totalclicks += session["problem"]["steps"]

            problemkey = get_problemkey(session["problem"])
            records[problemkey].append([session["problem"], session["env"], session["history"], endtime])

            c = Counter()

            for record in records[problemkey]:
                c[record[1]["score"]] += 1

            sortedrecords = sorted(c.items(), key=lambda item:item[0], reverse=True)

            for i, record in enumerate(sortedrecords):
                if record[0] == session["env"]["score"]:
                    index = i

            session["env"] = None
            sendj("records", {"records":sortedrecords, "index":index})
        else:

            # TODO: Send all simultaneously?
            options = check_options(session["problem"], session["env"])
            sendj("options", options)
            if "__builtins__" in session["env"]:
                del session["env"]["__builtins__"]
            sendj("env", session["env"])

    elif j["type"] == "continue":
        sendj("problems", problems)
        sendj("stats", stats())


try:
    with open(RECORDFILE) as recordfile:
        lines = recordfile.read().splitlines()

        for line in lines:
            line = json.loads(line)
            problemkey = get_problemkey(line[0])
            records[problemkey].append(line)
except FileNotFoundError:
    with open(RECORDFILE, "w+") as recordfile:
        pass

from time import time

tstart = time()
totalgames = 3450
totalclicks = 85585
for problemkey, lst in records.items():
    for eh in lst:
        totalgames += 1
        totalclicks += len(eh[2])

print(time()-tstart)

print(totalgames, "total games")
print(totalclicks, "total clicks")

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")
