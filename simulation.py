from random import choice, randint
import json
import base64
import zlib
from time import sleep

from io_utils import NonBlockingInput

def check_options(problem, env):
    options = []
    for index, thing in enumerate(problem["oneof"]):
        options.append(all([condition(env) for condition in thing[1]]))
    return options

def single_step(problem, env, history, decisionfunc):
	env["step"] = env.get("step", 0) + 1
	step = env["step"]

	if callable(decisionfunc):
		decisionindex = decisionfunc(problem, env, history, step)
	elif isinstance(decisionfunc, int):
		decisionindex = decisionfunc
	else:
		# assume string
		for index, decision in enumerate(problem["oneof"]):
			if decision[0] == decisionfunc:
				decisionindex = index
				break
		else:
			raise ValueError("Invalid decision name", decisionfunc)

	decision = problem["oneof"][decisionindex]
	history.append(decisionindex)#[step, decisionindex])#also have to add invalid decisions
	# TODO: allow null/None decision?
	# TODO: specify behavior on invalid decisions
	if all([condition(env) for condition in decision[1]]):
		for effect in decision[2]:
			effect(env)

	for thing in problem["always"]:
		if all([condition(env) for condition in thing[1]]):
			for effect in thing[2]:
				effect(env)

	env["score"] = problem["score"](env)

	return env, history

def run(problem, decisionfunc):

	env = {}
	history = []

	for step in range(problem["steps"]):

		env, history = single_step(problem, env, history, decisionfunc)

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

def df_player_nowait_wrapper():

	nbi = NonBlockingInput(exit_condition='quit')

	def df_player_nowait(problem, env, history, step):

		print("Step:", step, "\tScore:", problem["score"](env))

		sleep(1)

		decisionindex = None

		if nbi.input_queued():
			inp = nbi.input_get()
			print("GOT", inp)
			try:
				inp = int(inp)
				if 0 <= inp < len(problem["oneof"]):
					decisionindex = inp
			except ValueError:
				pass

		return 0 if decisionindex == None else decisionindex

	return df_player_nowait

def playergame(problem, step):

	if step:
		decisionfunc = df_player
	else:

		decisionfunc = df_player_nowait_wrapper()

	env, history = run(problem, decisionfunc=decisionfunc)

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
