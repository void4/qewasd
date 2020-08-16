from copy import deepcopy
from math import prod

def atleast(key, value):
	def eval(env):
		if key not in env:
			return False
		return env[key] >= value
	return eval

def atleastkey(key, key2):
	def eval(env):
		if key not in env:
			return False
		return env[key] >= env[key2]
	return eval


def equal(key, value):
	def eval(env):
		if key not in env:
			return value == 0
		return env[key] == value
	return eval

def setkey(key, value):
	def eval(env):
		env[key] = value

	return eval

def add(key, value):
	def eval(env):
		if key in env:
			env[key] += value
		else:
			env[key] = value

	return eval

def multiply(key1, key2):
	def eval(env):
		return env.get(key1, 0) * env.get(key2, 0)

	return eval

def multiplyMany(key1, *keys):
	def eval(env):
		return env.get(key1, 0) * prod([env.get(key, 0) for key in keys])

	return eval

def addMultiply(key,key2,multiplier):
	def eval(env):
		if key2 not in env:
			return

		env[key] += env[key2] * multiplier

	return eval

def setMultiply(key,key2,multiplier):
	def eval(env):
		if key2 not in env:
			return

		env[key] = env[key2] * multiplier

	return eval

def get(key):
	def eval(env):
		if key not in env:
			return 0

		return env[key]

	return eval

functions = {
	"atleast": atleast,
	"atleastkey": atleastkey,
	"add": add,
	"addMultiply": addMultiply,
	"get": get,
	"equal": equal,
	"setkey": setkey,
	"multiply": multiply,
	"setMultiply": setMultiply,
	"multiplyMany": multiplyMany,
}

def convert_function(f):
	if f[0] not in functions:
		raise ValueError("Unknown function", name)

	return functions[f[0]](*f[1:])

def element_replace(l, i, f):
	l[i] = convert_function(f)

def key_replace(d, k, f):
	d[k] = convert_function(f)

def convert(sproblem):
	problem = deepcopy(sproblem)
	for triple in problem["oneof"]:
		for i, condition in enumerate(triple[1]):
			print(i, condition)
			element_replace(triple[1], i, condition)
		for i, effect in enumerate(triple[2]):
			element_replace(triple[2], i, effect)

	for triple in problem["always"]:
		for i, condition in enumerate(triple[1]):
			element_replace(triple[1], i, condition)
		for i, effect in enumerate(triple[2]):
			element_replace(triple[2], i, effect)

	key_replace(problem, "score", problem["score"])

	return problem
