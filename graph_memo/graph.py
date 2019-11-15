from typing import Dict, List, Tuple
import networkx as nx


def compose_graph(nodes: List[str],
                  edges: List[Tuple[str, str]],
                  attributes: List[Dict]):
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    for node, attribute in zip(nodes, attributes):
        for key, value in attribute.items():
            nx.set_node_attributes(graph, node, value)

    return graph
