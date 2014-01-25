graph-matching
==============

An implementation of the 'Matching with our Eyes Closed' algorithm (based on and named after [this paper](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/38289.pdf)) for generating a randomized matching for a non-bipartite graph in an online manner.

As the algorithm is randomized, the matchings produced are not guaranteed to be optimal, but rather, have expected size of at least 0.56 of the largest possible.

Graphical evidence is provided using the [NetworkX](http://networkx.github.io) and [Matplotlib](http://matplotlib.org) packages.
