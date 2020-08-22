from collections import defaultdict, Counter
from copy import deepcopy
import json
from time import time
import os

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, send, emit

from problems import problems
from simulation import single_step, check_options
from database import get_problemkey

RECORDFILE = "records.txt"
RPSRECORDFILE = "rpsrecords.txt"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# TODO: Redis
#sessions = {}

rps_players = []
rps_games = []

def get_game(sid):
    for game in rps_games:
        if sid in [player["id"] for player in game]:
            return game

def delete_game(sid):
    # Race conditions galore
    game = get_game(sid)
    with open(RPSRECORDFILE, "a" if os.path.exists(RPSRECORDFILE) else "w") as recordfile:
        recordfile.write(json.dumps(game)+"\n")
    rps_games.remove(game)

def sendjall(typ, j, game, *args, **kwargs):
    for player in game:
        sendj(typ, j, room=player["id"], *args, **kwargs)

def rps_match(seeking):
    #for player in list(rps_players):
    if len(rps_players) > 0:
        player = rps_players[0]
        #if player["status"] == "waiting":
        #rps_players.remove(seeking)
        rps_players.remove(player)
        game = [{"id":seeking, "score":0, "history":[]}, {"id":player, "score":0, "history":[]}]
        rps_games.append(game)
        return game

    rps_players.append(seeking)
    return None

def sendj(typ, j, *args, **kwargs):
    send({"type":typ, "data":j}, json=True, *args, **kwargs)

"""
pid = 0
def player_id():
    global pid
    pid += 1
    return pid
"""

@socketio.on('connect')
def handle_connect():
    print('connected', request.sid)
    #session["id"] = player_id()
    sendj("problems", problems)
    sendj("stats", stats())
    #sessions[request.sid] = session

@socketio.on('disconnect')
def handle_disconnect():
    print("disconnected", request.sid)
    game = get_game(request.sid)
    if game is not None:
        sendjall("rps-status", None, game)
        delete_game(request.sid)

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

    elif j["type"] == "continue_rps":
        game = get_game(request.sid)
        sendjall("rps-status", None, game)
        delete_game(request.sid)

    elif j["type"] == "rps":
        game = rps_match(request.sid)
        if game is None:
            sendj("rps-status", "matching")
        else:
            sendjall("rps-status", "match", game)
            #session["rpsgame"] = game
            # Doesn't work
            #sessions[game[0]["id"] if game[0]["id"]!=request.sid else game[1]["id"]]["rpsgame"] = game
    elif j["type"] == "rps_action":
        game = get_game(request.sid)#session["rpsgame"]
        data = j["data"]
        player, other = game if game[0]["id"] == request.sid else game[::-1]
        player["decision"] = data
        print(game)
        if "decision" in other:
            d1 = player["decision"]
            d2 = other["decision"]

            # TODO check validity of values

            player["history"].append(d1)
            other["history"].append(d2)

            if d1 == d2:
                # Tie
                #sendjall("rps-update", {"phase":0, "status":"tie", game)

                del player["decision"]
                del other["decision"]

                sendj("rps-update", {"phase": 0, "status":"tie", "score":player["score"], "other": other["score"]}, room=player["id"])
                sendj("rps-update", {"phase": 0, "status":"tie", "score":other["score"], "other": player["score"]}, room=other["id"])

                return
            elif (d1+1)%3 == d2:
                winner = other
                loser = player
            else:
                winner = player
                loser = other

            winner["score"] += 1

            names = ["rock", "paper", "scissors"]

            dw = names[winner["decision"]]
            dl = names[loser["decision"]]

            del winner["decision"]
            del loser["decision"]

            sendj("rps-update", {"phase": 0, "status": f"win! - loser chose {dl}", "score":winner["score"], "other": loser["score"]}, room=winner["id"])
            sendj("rps-update", {"phase": 0, "status": f"lost! - winner chose {dw}", "score":loser["score"], "other": winner["score"]}, room=loser["id"])

        else:
            sendj("rps-update", {"phase": 1, "status":"Waiting for other player...", "score":player["score"]}, room=player["id"])


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
