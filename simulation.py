from random import choice, randint
import json
import base64
import zlib
from time import sleep
from copy import deepcopy

from io_utils import NonBlockingInput

def check_options(problem, env):
	options = []
	for index, thing in enumerate(problem["oneof"]):
		options.append(True if thing[1] == "" else eval(thing[1], env))

	if "__builtins__" in env:
		del env["__builtins__"]
		
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
	if decision[1] == "" or eval(decision[1], env):
		exec(decision[2], {}, env)

	for regular in problem["always"]:
		if regular[1] == "" or eval(regular[1], env):
			exec(regular[2], {}, env)

	env["score"] = eval(problem["score"], env)

	if "__builtins__" in env:
		del env["__builtins__"]

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

	env = deepcopy(problem.get("start", {}))
	history = []

	for decisionindex in truehistory:
		env, history = single_step(problem, env, history, decisionindex)

	return env, history

def treeplay(problem, truehistory):

	env = deepcopy(problem.get("start", {}))
	env["score"] = 0
	env["step"] = 0
	history = []

	envs = [deepcopy(env)]

	for decisionindex in truehistory:
		env, history = single_step(problem, env, history, decisionindex)
		envs.append(deepcopy(env))

	return envs, history

def df_rand(problem, env, history, step):
	options = check_options(problem, env)
	return choice([index for index, value in enumerate(options) if value])

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
	print("Replay env", r_env)
	print("Replay history", r_history)
	return r_env, r_history

def decompress(history):
	return json.loads(zlib.decompress(base64.urlsafe_b64decode(history.encode("utf8"))).decode("utf8"))

def compress(history):
	return base64.urlsafe_b64encode(zlib.compress(json.dumps(history).encode("utf8"))).decode("utf8")
