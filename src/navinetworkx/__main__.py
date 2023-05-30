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

    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_edge(1,2)
    print(G)
    G.add_nodes_from([3,4,5])
    G.add_edges_from([(3,4),(4,5)])
    print(G)
    print(G.neighbors(3))

    G = nx.Graph()
    G.add_edge("A", "B", weight=4)
    G.add_edge("B", "D", weight=2)
    G.add_edge("A", "C", weight=3)
    G.add_edge("C", "D", weight=4)
    print(nx.shortest_path(G, "A", "D", weight="weight"))


if __name__ == "__main__":
    main()
