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

def get(key):
	def eval(env):
		if key not in env:
			return 0

		return env[key]

	return eval

functions = {
	"atleast": atleast,
	"add": add,
	"addMultiply": addMultiply,
	"get": get,
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
	for pair in problem["oneof"]:
		for i, condition in enumerate(pair[0]):
			element_replace(pair[0], i, condition)
		for i, effect in enumerate(pair[1]):
			element_replace(pair[1], i, effect)

	for pair in problem["always"]:
		for i, condition in enumerate(pair[0]):
			element_replace(pair[0], i, condition)
		for i, effect in enumerate(pair[1]):
			element_replace(pair[1], i, effect)

	key_replace(problem, "score", problem["score"])

	return problem
