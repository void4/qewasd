import json

def get_problemkey(problem):
    # finding equivalence is hard, because item names might be different
    indices = "steps start oneof always".split()
    p = {}
    for index in indices:
        p[index] = problem[index]

    return json.dumps(p)
