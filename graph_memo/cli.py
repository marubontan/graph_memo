from .parser import load_all_memos, compose_nodes_and_edges
from .graph import compose_graph
import pdb


def main():
    memos = load_all_memos()
    nodes, edges, attributes = compose_nodes_and_edges(memos)
    graph = compose_graph(nodes, edges, attributes)
    pdb.set_trace()
