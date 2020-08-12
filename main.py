from random import choice
from collections import defaultdict

env = {}

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

# conditions, effects
decisions = [
	((),(add("money",1),)),#manual click
	((atleast("money",5),), (add("money", -5), add("ship", 1))),#buy ship
	((atleast("ship",1),),(add("money",3),add("ship",-1))),#sell ship
]

always = [
	((), (addMultiply("money", "ship", 3),)),
]

SIMS = 1000
MAXSTEPS = 100

record = None
recordhistory = None

for sim in range(SIMS):

	env = {}
	
	history = []

	for step in range(MAXSTEPS):
	
		for thing in always:
			if all([condition(env) for condition in thing[0]]):
				for effect in thing[1]:
					effect(env)
	
		decision = choice(decisions)
		if all([condition(env) for condition in decision[0]]):
			history.append((step, decision))
			for effect in decision[1]:
				effect(env)

	if record is None or env["money"] > record:
		print("New record:", env)
		record = env["money"]
		recordhistory = history
