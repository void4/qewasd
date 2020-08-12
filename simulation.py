from random import choice, randint
import json
import base64
import zlib

def run(problem, decisionfunc):

	env = {}
	history = []

	for step in range(problem["steps"]):

		env["step"] = step

		for thing in problem["always"]:
			if all([condition(env) for condition in thing[0]]):
				for effect in thing[1]:
					effect(env)

		decisionindex = decisionfunc(problem, env, history, step)

		decision = problem["oneof"][decisionindex]
		history.append(decisionindex)#[step, decisionindex])#also have to add invalid decisions
		# TODO: allow null/None decision?
		if all([condition(env) for condition in decision[0]]):
			for effect in decision[1]:
				effect(env)

	return env, history

def df_player(problem, env, history, step):
	print(env, history, step)

	decisionindex = None
	while not isinstance(decisionindex, int) or not (0 <= decisionindex < len(problem["oneof"])):
		try:
			decisionindex = int(input(">"))
		except ValueError:
			continue

	return decisionindex

def df_player_nowait(problem, env, history, step):
	raise NotImplementedError("Not implemented yet!")

def playergame(problem, step):
	decisionfunc = df_player if step else df_player_nowait
	env, history = run(problem, decisionfunc=df_player)

def replay(problem, truehistory):
	def df_history(problem, env, history, step):
		"""
		for pair in truehistory:
			if pair[0] == step:
				return pair[1]
		"""
		return truehistory[step]
	return run(problem, decisionfunc=df_history)

def df_rand(problem, env, history, step):
	return randint(0, len(problem["oneof"])-1)

def simgame(problem, sims=1000):

	record = None
	recordhistory = None

	for sim in range(sims):

		env, history = run(problem, decisionfunc=df_rand)

		score = problem["score"](env)
		if record is None or score > record:
			print("New record:", score, env)#, history)#sim,
			record = score
			recordhistory = history

	print("Replaying record...")
	r_env, r_history = replay(problem, recordhistory)
	print(r_env)
	print(r_history)
	return r_env, r_history

def decompress(history):
	return json.loads(zlib.decompress(base64.urlsafe_b64decode(history.encode("utf8"))).decode("utf8"))

def compress(history):
	return base64.urlsafe_b64encode(zlib.compress(json.dumps(history).encode("utf8"))).decode("utf8")
