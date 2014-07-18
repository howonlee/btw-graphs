import numpy as np
import numpy.random as npr

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot

import networkx as nx

class Sand(object):
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
		This works!
		Now, to make the graphical model corresponding to the stored "graphs" here
		the "graphs" are really the series of coordinates of the avalanching sand
		"""
		graphs = set()
		if x < 0 or x >= self.n or y < 0 or y >= self.n:
			return set()
		self.array[x][y] += 1
		if self.array[x][y] >= self.critLevel:
			graphs.add((x,y))
			self.numAvalanches += 1
			self.array[x][y] -= 4
			graphs.union(self.increase(x+1, y))
			graphs.union(self.increase(x-1, y))
			graphs.union(self.increase(x, y+1))
			graphs.union(self.increase(x, y-1))
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
		self.fig.canvas.manager.window.after(1000, self.animate_callback)
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

	def info(self):
		print "order: ", self.graph.order()
		print "size: ", self.graph.size()

if __name__ == '__main__':
	sand = Sand(n=5000, critLevel=4)
	sand.loop(steps=100000)
	graph = SandGraph(sand.graphs)
	graph.info()
	#viewer = SandViewer(sand)
	#viewer.animate(1000)

