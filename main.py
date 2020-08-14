from functions import convert
from simulation import simgame, playergame, compress, decompress

# conditions, effects
sproblem = {
	"steps": 25,

	"oneof" : [
		["do nothing", [],[]],
		["manual click", [],[["add", "money",1],]],
		["buy ship", [["atleast", "money",10],], [["add", "money", -10], ["add", "ship", 1]]],
		["sell ship", [["atleast", "ship",1],],[["add", "money", 5], ["add", "ship", -1]]],
		["buy factory", [["atleast", "money",20],], [["add", "money", -20], ["add", "factory", 1]]],
		["sell factory", [["atleast", "factory",1],],[["add", "money", 10], ["add", "factory", -1]]],
	],

	"always" : [
		["ship income", [], [["addMultiply", "money", "ship", 3],]],
		["factory income", [], [["addMultiply", "money", "factory", 5],]],
	],

	"score": ["get", "money"]
}

problem = convert(sproblem)

if __name__ == "__main__":
	env, history = simgame(problem, 1000)
	print(compress(history))
	playergame(problem, step=False)
