import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot

import networkx as nx
from sand import Sand, SandGraph

if __name__ == '__main__':
	#generate the text
	# I don't really know how
	s = Sand(n=3000, critLevel=4)
	s.loop(steps=1500)
	grph = SandGraph(s.graphs)
	take the graph
	make words out of it with a markov-like process?
	associate centralities with frequencies, then randomly walk the chain
	maybe grammar will come spiralling out of it

