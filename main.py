from random import choice, randint
from collections import defaultdict
from copy import deepcopy

def atleast(key, value):
	def eval(env):
		if key not in env:
			return False
		return env[key] >= value
	return eval

def add(key, value):
	def eval(env):
		if key in env:
			env[key] += value
		else:
			env[key] = value

	return eval

def addMultiply(key,key2,multiplier):
	def eval(env):
		if key2 not in env:
			return

		env[key] += env[key2] * multiplier

	return eval

functions = {
	"atleast": atleast,
	"add": add,
	"addMultiply": addMultiply,
}

# conditions, effects
sproblem = {
	"steps": 100,
	"oneof" : [
		#[[],[]],#do nothing
		[[],[["add", "money",1],]],#manual click
		[[["atleast", "money",5],], [["add", "money", -5], ["add", "ship", 1]]],#buy ship
		[[["atleast", "ship",1],],[["add", "money", 3], ["add", "ship", -1]]],#sell ship
	],

	"always" : [
		[[], [["addMultiply", "money", "ship", 3],]],
	]
}

def replace(l, i, f):
	if f[0] not in functions:
		raise ValueError("Unknown function", name)

	l[i] = functions[f[0]](*f[1:])

def convert(sproblem):
	problem = deepcopy(sproblem)
	for pair in problem["oneof"]:
		for i, condition in enumerate(pair[0]):
			replace(pair[0], i, condition)
		for i, effect in enumerate(pair[1]):
			replace(pair[1], i, effect)

	for pair in problem["always"]:
		for i, condition in enumerate(pair[0]):
			replace(pair[0], i, condition)
		for i, effect in enumerate(pair[1]):
			replace(pair[1], i, effect)

	return problem

problem = convert(sproblem)

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
		history.append((step, decisionindex))#also have to add invalid decisions
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

def playergame():
	env, history = run(problem, decisionfunc=df_player)

def replay(truehistory):
	def df_history(problem, env, history, step):
		for pair in truehistory:
			if pair[0] == step:
				return pair[1]

	return run(problem, decisionfunc=df_history)

def df_rand(problem, env, history, step):
	return randint(0, len(problem["oneof"])-1)

def simgame():

	SIMS = 10000

	record = None
	recordhistory = None

	for sim in range(SIMS):

		env, history = run(problem, decisionfunc=df_rand)

		if record is None or env["money"] > record:
			print("New record:", env)#, history)#sim,
			record = env["money"]
			recordhistory = history

	print("Replaying record...")
	r_env, r_history = replay(recordhistory)
	print(r_env)


simgame()
playergame()
