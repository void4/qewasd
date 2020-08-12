from functions import convert
from simulation import simgame, playergame, compress, decompress

# conditions, effects
sproblem = {
	"steps": 100,

	"oneof" : [
		[[],[]],#do nothing
		[[],[["add", "money",1],]],#manual click
		[[["atleast", "money",10],], [["add", "money", -10], ["add", "ship", 1]]],#buy ship
		[[["atleast", "ship",1],],[["add", "money", 5], ["add", "ship", -1]]],#sell ship
		[[["atleast", "money",20],], [["add", "money", -20], ["add", "factory", 1]]],#buy factory
		[[["atleast", "factory",1],],[["add", "money", 10], ["add", "factory", -1]]],#sell factory
	],

	"always" : [
		[[], [["addMultiply", "money", "ship", 3],]],#ship income
		[[], [["addMultiply", "money", "factory", 5],]],#factory income
	],

	"score": ["get", "money"]
}

problem = convert(sproblem)

env, history = simgame(problem, 10000)
print(compress(history))
playergame(problem, step=True)
