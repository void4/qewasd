from random import choice, randint

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

def playergame(problem):
	env, history = run(problem, decisionfunc=df_player)

def replay(problem, truehistory):
	def df_history(problem, env, history, step):
		for pair in truehistory:
			if pair[0] == step:
				return pair[1]

	return run(problem, decisionfunc=df_history)

def df_rand(problem, env, history, step):
	return randint(0, len(problem["oneof"])-1)

def simgame(problem):

	SIMS = 10000

	record = None
	recordhistory = None

	for sim in range(SIMS):

		env, history = run(problem, decisionfunc=df_rand)

		score = problem["score"](env)
		if record is None or score > record:
			print("New record:", score, env)#, history)#sim,
			record = score
			recordhistory = history

	print("Replaying record...")
	r_env, r_history = replay(problem, recordhistory)
	print(r_env)
