from copy import deepcopy

from problems import problems


def l2s(l):
    s = ""
    for x in l:
        if isinstance(x, str):
            s += x
        elif isinstance(x, int):
            s += str(x)

        s += " "

    return s[:-1]

def stof(sproblem):
    p = deepcopy(sproblem)
    for di, decision in enumerate(p["oneof"]):
        p["oneof"][di][1] = ", ".join([l2s(c) for c in p["oneof"][di][1]])
        p["oneof"][di][2] = ", ".join([l2s(c) for c in p["oneof"][di][2]])

    for di, decision in enumerate(p["always"]):
        p["always"][di][1] = ", ".join([l2s(c) for c in p["always"][di][1]])
        p["always"][di][2] = ", ".join([l2s(c) for c in p["always"][di][2]])


    return p

if __name__ == "__main__":
    print(stof(problems[4]))
