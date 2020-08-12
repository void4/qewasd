from random import choice, randint
from collections import defaultdict

from functions import convert

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
