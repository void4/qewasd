from functions import convert
from simulation import simgame, playergame

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
	],

	"score": ["get", "money"]
}

problem = convert(sproblem)

simgame(problem)
playergame(problem)
