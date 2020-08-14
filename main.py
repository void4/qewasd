from functions import convert
from simulation import simgame, playergame, compress, decompress
from problems import problems

if __name__ == "__main__":
	problem = convert(problems[0])
	env, history = simgame(problem, 1000)
	print(compress(history))
	playergame(problem, step=False)
