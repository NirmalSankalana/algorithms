import random
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(n_nodes, alpha = 0.5):
    G = nx.MultiDiGraph()
    G.add_nodes_from(range(n_nodes))
    for i in range(n_nodes):
        for j in range(i+1,n_nodes):
            if random.random() < alpha:
                weight=random.randint(1,10)
                G.add_edge(i, j, weight=weight)

            if random.random() < alpha:
                weight=random.randint(1,10)
                G.add_edge(j, i, weight=weight)
    return G
  

def display_graph(G):
    pos = nx.spring_layout(G)  
    weight_labels = nx.get_edge_attributes(G, 'weight')  
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_labels)  
    plt.show()


n_nodes = 5
G = create_graph(n_nodes, alpha = 0.5)
display_graph(G)