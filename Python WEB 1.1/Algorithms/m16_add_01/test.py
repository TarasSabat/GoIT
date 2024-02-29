import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

graph.add_node("Oleksandr")
graph.add_node("Krabaton")
graph.add_node("Nataliya")
graph.add_node("Valdemar")
graph.add_node("Bogdan")
graph.add_node("Anastasiya")

graph.add_edge("Oleksandr", "Krabaton")
graph.add_edge("Nataliya", "Anastasiya")
graph.add_edge("Valdemar", "Bogdan")
graph.add_edge("Bogdan", "Krabaton")
graph.add_edge("Bogdan", "Anastasiya")

nx.draw(graph, with_labels=True)
plt.axis('off')
plt.show()