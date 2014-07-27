import numpy as np
import numpy.random as npr
import uuid
import collections

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot

import networkx as nx

class SandNet(object):
	"""
	Bak Tang Wiesenfeld self-organized criticality model for networks here
	Not to be confused with the sand-graph in the sand model, which _makes_ a graph _from_ the lattice
	here, there is no lattice, just the graph
	"""
	def __init__(self, n, critLevel):
		self.n = n
		self.critLevel = critLevel
		self.graph = nx.Graph() #maybe directed?
		self.numAvalanches = 0

	def loop(self, steps=1):
		[self.step() for i in xrange(steps)]

	def increase(self, x, y):
		graphs = collections.Counter()
		if x < 0 or x >= self.n or y < 0 or y >= self.n:
			return collections.Counter()
		self.array[x][y] += 1 # something
		if self.array[x][y] >= self.critLevel: #something
			the above critlevel node.val -= 4
			for each neighboring node from the above critlevel node:
				self.numAvalanches += 1
				increase(node)

	def step(self):
		stepgraph = self.increase(npr.randint(self.n-1), npr.randint(self.n-1))

class SandViewer(object):
	"""
	use the networkx viewer
	"""
	def __init__(self, sand, cmap=matplotlib.cm.gray_r):
		self.sand = sand
		self.cmap = cmap
		self.fig = pyplot.figure()
		pyplot.axis([0, sand.n, 0, sand.n])
		pyplot.xticks([])
		pyplot.yticks([])
		self.pcolor = None
		self.update()

	def update(self):
		if self.pcolor:
			self.pcolor.remove()
		a = self.sand.array
		self.pcolor = pyplot.pcolor(a, vmax=10, cmap=self.cmap)
		self.fig.canvas.draw()
		#print self.sand.graphs

	def animate(self, steps=10):
		self.steps = steps
		self.fig.canvas.manager.window.after(10, self.animate_callback)
		pyplot.show()

	def animate_callback(self):
		for i in range(self.steps):
			self.sand.step()
			self.update()

if __name__ == '__main__':
	#make the graphs
	#investigate the properties of the graphs
	i = 3
	sand = Sand(n=i*1000, critLevel=4)
	sand.loop(steps=i*500)
	print "loop ", i, " done"
	print "===================="
	graph = SandGraph(sand.graphs)
	graph.show_largest_component("large_component.pdf")
	#graph.subcomponent_stats()
	#graph.degree_dist()
	#print sand.graphs
	#sand.loop(steps=20000)
	#viewer = SandViewer(sand)
	#viewer.animate(10000)
