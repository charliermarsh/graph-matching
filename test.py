import unittest
from random import random
from graph import Graph


def randomGraph(n, p):
    g = Graph(n)
    for u in range(n):
        for v in range(u + 1, n):
            if random() <= p:
                g.connect(u, v)
    return g


class GraphTest(unittest.TestCase):

    def validMatching(self, g, matching):
        def trueEdges(g, matching):
            for (u, v) in matching:
                self.assertTrue(g.adjacent(u, v))

        def uniqueVertices(g, matching):
            for (u, v) in matching:
                print(u, v)
                for (x, y) in matching:
                    if (x, y) == (u, v):
                        continue

                    self.assertNotEqual(x, u)
                    self.assertNotEqual(x, v)
                    self.assertNotEqual(y, u)
                    self.assertNotEqual(y, v)

        trueEdges(g, matching)
        uniqueVertices(g, matching)

    def testMatching(self):
        g = randomGraph(20, 0.1)
        matching = g.randomMatching()
        self.validMatching(g, matching)
        g.plotMatching()

if __name__ == "__main__":
    unittest.main()
