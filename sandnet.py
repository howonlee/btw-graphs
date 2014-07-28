import numpy as np
import numpy.random as npr
from random import choice
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
	def __init__(self, corpus, critLevel):
		self.corpus = corpus
		self.critLevel = critLevel
		self.graph = nx.DiGraph()
		for word in corpus:
			go through the graph and make the graph
		#initialize the graph properly
		self.numAvalanches = 0

	def loop(self, steps=1):
		return [self.step() for i in xrange(steps)]

	def increase(self, chosenNode):
		chosenNode.sandval += 1
		words = []
		if chosenNode.sandval >= self.critLevel: #something
			chosenNode.sandval -= 4
			words.append(chosenNode.word)
			for neighbor in nx.DiGraph.neighbors(chosenNode):
				self.numAvalanches += 1
				words = words + increase(neighbor)
		return words

	def step(self):
		return self.increase(choice(self.graph.nodes()))

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
	with open(something) as corpusFile:
		corpus = corpusFile.readAll().split()
		net = SandNet(corpus=corpus, critLevel=4)
		output = net.loop(steps=1000)
		print " ".join(output)
