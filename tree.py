# Construct decision tree
import json
from time import time
from math import e,log,sin,cos

import networkx as nx
import matplotlib.pyplot as plt

from simulation import treeplay
from server import records
from database import get_problemkey

def draw(problemkey):

    posdict = {}
    namedict = {}

    g = nx.MultiDiGraph()

    sortedrecords = sorted(records[problemkey], key=lambda record:record[1]["score"], reverse=True)

    top = 5

    for record in sortedrecords[:top]:
        problem = record[0]
        envs, history = treeplay(problem, record[2])

        # TODO: sort keys! - they'll have the same position already
        senvs = [str(n) for n in envs]

        g.add_nodes_from(senvs)

        for i,h in enumerate(history):
            g.add_edge(senvs[i], senvs[i+1])
            namedict[(senvs[i], senvs[i+1])] = problem["oneof"][h][0]


        for i, env in enumerate(envs):
            # Linear
            posdict[senvs[i]] = [env["step"], env["score"]]#1.01**env["score"])#log(1+env["score"]))

            """
            # Angular
            step = env["step"]
            score = env["score"]**0.5

            posdict[senvs[i]] = [sin(step/2)*score, cos(step/2)*score]
            """

    normalize = 0
    if normalize:
        # Normalization
        posdict2 = {}
        while len(posdict) > 0:
            node = list(posdict.keys())[0]
            x,y = posdict.pop(node)

            miy = y
            may = y

            nodes = [[node, [x,y]]]

            for key, value in list(posdict.items()):
                if value[0] == x:
                    posdict.pop(key)
                    x,y = value
                    if y < miy:
                        miy = y

                    if y > may:
                        may = y

                    nodes.append([key, value])

            for kv in nodes:
                if may-miy != 0:
                    kv[1][1] = (kv[1][1]-miy)/(may-miy) * 100
                posdict2[kv[0]] = kv[1]

        posdict = posdict2

    # use step as angle and score as radius?!

    plt.figure()
    plt.title(problem["name"] + " - Top "+str(top))
    pos = nx.spring_layout(g, pos=posdict, fixed=list(posdict.keys()))
    #pos = nx.planar_layout(g)
    #pos = nx.spectral_layout(g)
    #pos = nx.spiral_layout(g)
    # layout by similarity?/distance, use edge weight
    nx.draw(g, pos, edge_color=(0.5,0.5,0.5), node_size=50, node_color=(0.0,0.0,0.5,0.3))
    nx.draw_networkx_labels(g, pos, font_size=6)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=namedict, font_size=5)
    plt.savefig(f"graphs/{int(time()*1000)}.png", dpi=500)
    plt.show()

if __name__ == "__main__":
    draw(list(records.keys())[1])
    print(len(list(records.values())[1]))
