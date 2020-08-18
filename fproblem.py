from copy import deepcopy

from problems import problems


def l2s(l):
    if l[0] in ["atleast", "atleastkey"]:
        return l[1] + " >= " + str(l[2])
    elif l[0] == "atmost":
        return l[1] + " <= " + str(l[2])
    elif l[0] == "add":
        if l[2] >= 0:
            return l[1] + " += " + str(l[2])
        else:
            return l[1] + " -= " + str(-l[2])
    elif l[0] == "addkey":
        return l[1] + " += " + l[2]
    elif l[0] == "addMultiply":
        return l[1] + " += " + l[2] + " * " + str(l[3])
    else:
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
