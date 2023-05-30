#!/usr/bin/env python3
"""
navinetworkx
"""
import argparse
import networkx as nx

def main():
    """
    entry point
    """
    parser = argparse.ArgumentParser(description='do something')
    parser.add_argument('--demo', action='store_true', help='Generate Demo Msg')
    args = parser.parse_args()

    if args.demo:
        print("Demo")

    graph = nx.Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1,2)
    print(graph)
    graph.add_nodes_from([3,4,5])
    graph.add_edges_from([(3,4),(4,5)])
    print(graph)
    print(graph.neighbors(3))

    graph = nx.Graph()
    graph.add_edge("A", "B", weight=4)
    graph.add_edge("B", "D", weight=2)
    graph.add_edge("A", "C", weight=3)
    graph.add_edge("C", "D", weight=4)
    print(nx.shortest_path(graph, "A", "D", weight="weight"))


if __name__ == "__main__":
    main()
