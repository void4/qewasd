from functions import convert
from simulation import simgame, playergame, compress, decompress
from problems import problems

if __name__ == "__main__":
	problem = convert(problems[3])
	print(problem["name"])
	env, history = simgame(problem, 100000)
	#print(compress(history))
	#playergame(problem, step=False)
