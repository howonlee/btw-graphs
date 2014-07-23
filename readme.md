Bak-Tang-Wiesenfeld graphs
====

This is the "abelian sandpile" automaton for making 1/f noise-like shapes (fractal shapes). It works like it does in Wikipedia. However, there is also a way to think about the automaton as a sort of graph generator. If you drop the sand on the sandpile randomly, you make a random graph. This is because there is a relation you can think of between one square, which has the pile of sand with value >= 4 which is toppling, and the squares around it. Those relations can be the edges in a graph where the nodes are the squares themselves.

The properties of this graph are sort of interesting: it's not quite like Erdos-Renyi graphs, it's not quite like Barabasi-Albert graphs. They seem, given the numbers, to have a power law degree distribution, not too much increasing average path length, and small enough clustering coefficient, I think. No proofs or anything, just looking at a bunch of generated graphs.

Just take a look at them. They are pretty.
