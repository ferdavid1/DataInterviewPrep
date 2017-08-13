import networkx as nx

G = nx.Graph()
# add nodes (1,2,3) and edges (1,2), (1,3)
G.add_edges_from([(1,2),(1,3)])
c = nx.connected_components(G)
for node in c:
	print(node)