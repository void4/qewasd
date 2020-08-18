from server import records
from simulation import simgame, playergame, compress, decompress
from problems import problems


if __name__ == "__main__":
	for index, problem in enumerate(problems):
		print(index, problem["name"])
	print("------------------------------")
	for recordkey, record in records.items():
		print(record[0][0]["name"], len(record))

	problem = problems[4]
	print(problem["name"])
	input()
	env, history = simgame(problem, 100000)
	#print(compress(history))
	#playergame(problem, step=False)
