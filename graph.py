"""
    An implementation of the 'Matching with our Eyes Closed' algorithm
    for discovering random matchings in an online fashion for non-bipartite
    graphs. In this setting, the edges of the graph are not known beforehand,
    but we can query any pair to test for adjacency. If we find two, vertices
    that are indeed adjacent, we are committed to matching them. To emulate
    the scenario, our graph class is 'stupid' in that it doesn't store lists
    of edges, but rather, adjacencies.

    For more, see the original paper:
    http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/38289.pdf
"""

from random import shuffle
import networkx as nx
import matplotlib.pyplot as plt


class Graph(object):

    def __init__(self, n):
        """Initialize a graph on n nodes."""
        self.n = n
        self.e = [set() for i in range(n)]

    def connect(self, u, v):
        """Connects vertices u and v."""
        self.e[u].add(v)
        self.e[v].add(u)

    def adjacent(self, u, v):
        """Returns True if u and v are connected."""
        return u in self.e[v]

    def randomMatching(self):
        """
        Generate a matching using the randomized algorithm described
        in 'Matching with our Eyes Closed'.
        """

        # Generate random permutation of vertices
        permutation = range(self.n)
        shuffle(permutation)

        # Invert permutation list to get rank
        ranks = range(self.n)
        for idx, v in enumerate(permutation):
            ranks[v] = idx

        matched = set([])
        matches = set([])
        # Process in order of rank
        for v in ranks:
            if v in matched:
                continue

            def firstNeighbor(v):
                """Find highest-priority unmatched neighbor of v."""
                for u in ranks:
                    if u in matched or not self.adjacent(u, v):
                        continue

                    return u

            u = firstNeighbor(v)
            if u:
                # Add match between u, v
                matches.add((v, u))

                # Track matched vertices
                matched.add(v)
                matched.add(u)

        return matches

    def __toNetworkX(self):
        """Convert to a NetworkX representation (for plotting)."""
        G = nx.Graph()
        G.add_nodes_from(range(self.n))
        for u in range(self.n):
            for v in range(self.n):
                if self.adjacent(u, v):
                    G.add_edge(u, v)

        return G

    def plot(self):
        """Plot the graph."""
        G = self.__toNetworkX()
        pos = nx.shell_layout(G)
        nx.draw(G, pos)
        plt.show()

    def plotMatching(self, matching=None):
        """
        Plot a matching for the given graph. Matchings
        can be provided or generated within.

        Arguments:
        matching -- a matching for the graph (default None)
        """

        def splitNodes(matching):
            """Split into nodes in and out of matching."""
            outer = set(range(self.n))
            inner = set([])
            for (u, v) in matching:
                if u in outer:
                    outer.remove(u)
                if v in outer:
                    outer.remove(v)
                inner.add(u)
                inner.add(v)
            return list(inner), list(outer)

        def formatMatching(G, matching):
            inner, outer = splitNodes(matching)
            pos = nx.shell_layout(G)

            # Red = nodes in matching
            nx.draw_networkx_nodes(G, pos,
                                   nodelist=inner,
                                   node_color='r',
                                   node_size=500,
                                   alpha=0.8)

            # Blue = nodes _not_ in matching
            nx.draw_networkx_nodes(G, pos,
                                   nodelist=outer,
                                   node_color='b',
                                   node_size=500,
                                   alpha=0.3)

            # Highlight matching edges
            nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.3)
            nx.draw_networkx_edges(G, pos,
                                   edgelist=list(matching),
                                   width=8, alpha=0.5, edge_color='r')

        # Generate random matching, if not provided.
        if not matching:
            matching = self.randomMatching()
        # Convert to NetworkX
        G = self.__toNetworkX()

        formatMatching(G, matching)
        plt.show()
