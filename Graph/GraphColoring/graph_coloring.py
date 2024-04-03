import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def is_valid_coloring(G, coloring):
    for u, v in G.edges():
        if coloring[u] == coloring[v]:
            return False
    return True 



def greedy_coloring(G):
    coloring = {}
    for node in G.nodes():
        adjacent_colors = {coloring.get(v) for v in G.neighbors(node)}
        coloring[node] = next(color for color in itertools.count() if color not in adjacent_colors)
    return coloring


n_nodes = 10

G = nx.Graph()

G.add_nodes_from(range(n_nodes))

for i in range(n_nodes):
    for j in (i+1, n_nodes):
        if random.random() < 0.5:
            G.add_edge(i, j)


coloring_result = greedy_coloring(G)
print(coloring_result)
print(is_valid_coloring(G, coloring_result))

coloring_map = [coloring_result[node] for node in G.nodes()]
nx.draw(G, node_color=coloring_map, with_labels=True)
plt.show()