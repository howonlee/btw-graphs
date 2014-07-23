import numpy as np
import numpy.random as npr
import uuid
import collections

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot

import networkx as nx

class Sand(object):
	"""
	Bak Tang Wiesenfeld self-organized criticality model here for teh wins
	"""
	def __init__(self, n, critLevel):
		self.n = n
		self.critLevel = critLevel
		self.array = npr.randint(critLevel, size=(n, n))
		self.graphs = []
		self.numAvalanches = 0

	def get_array(self, start=0, end=None):
		if start==0 and end==None:
			return self.array
		else:
			return self.array[:, start:end]

	def loop(self, steps=1):
		[self.step() for i in xrange(steps)]

	def increase(self, x, y):
		"""
		Note dat recursive call
		f--ing up our ability to study anything about degree like 50,000
		"""
		graphs = collections.Counter()
		if x < 0 or x >= self.n or y < 0 or y >= self.n:
			return collections.Counter()
		self.array[x][y] += 1
		if self.array[x][y] >= self.critLevel:
			graphs[(x,y)] += 1
			self.numAvalanches += 1
			self.array[x][y] -= 4
			graphs += self.increase(x+1, y)
			graphs += self.increase(x-1, y)
			graphs += self.increase(x, y+1)
			graphs += self.increase(x, y-1)
		return graphs

	def step(self):
		stepgraph = self.increase(npr.randint(self.n-1), npr.randint(self.n-1))
		self.graphs.append(stepgraph)

class SandViewer(object):
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

class SandGraph(object):
	def __init__(self, graphList):
		self.graph = nx.Graph()
		for st in graphList:
			self.graph.add_edges_from(st)

	def degree_dist(self):
		print "order: ", self.graph.order()
		print "size: ", self.graph.size()
		pyplot.hist(nx.degree(self.graph).values(), log=True, bins=20)
		pyplot.title('degree histogram log plot')
		pyplot.show()

	def subcomponent_stats(self, g_bound=10):
		for g in nx.connected_component_subgraphs(self.graph):
			if g.order() < g_bound:
				continue
			print "g order: ", g.order()
			print "g size: ", g.order()
			print "average shortest path length: ", nx.average_shortest_path_length(g)
			print "path length ratio: ", nx.average_shortest_path_length(g) / g.order()
			print "clustering coeff: ", nx.average_clustering(g)

if __name__ == '__main__':
	#make the graphs
	#investigate the properties of the graphs
	for i in range(10):
		try:
			sand = Sand(n=i*1000, critLevel=4)
			sand.loop(steps=i*500)
			print "loop ", i, " done"
			print "===================="
			graph = SandGraph(sand.graphs)
			graph.subcomponent_stats()
			#graph.degree_dist()
		except:
			print "err"
	#print sand.graphs
	#sand.loop(steps=20000)
	#viewer = SandViewer(sand)
	#viewer.animate(10000)
