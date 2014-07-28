import numpy as np
import numpy.random as npr
from random import choice, randint
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
		prevWord = None
		wordct = collections.Counter()
		for word in corpus:
			wordct[word] += 1
			self.graph.add_node(word, sandval=randint(0, 4), word=word)
			if prevWord:
				self.graph.add_edge(prevWord, word)
			prevWord = word
		self.numAvalanches = 0

	def loop(self, steps=1):
		return [self.step() for i in xrange(steps)]

	def increase(self, chosenNode):
		"""
		Increase
		should be iterative, not recursive this time
		"""
		if type(chosenNode) == tuple:
			chosenData = self.graph.node[chosenNode[0]]
		elif type(chosenNode) == str:
			chosenData = self.graph.node[chosenNode]
		else:
			raise
		chosenData["sandval"] += 1
		words = ""
		if chosenData["sandval"] >= self.critLevel: #something
			self.numAvalanches += 1
			chosenData["sandval"] -= 4
			words = chosenData["word"]
			for neighbor in self.graph.neighbors(chosenData["word"]):
				words = words + " " + self.increase(neighbor)
		return words

	def step(self):
		return self.increase(choice(self.graph.nodes(data=True)))

if __name__ == '__main__':
	with open("corpus.txt", "r") as corpusFile:
		corpus = corpusFile.read().split()
		net = SandNet(corpus=corpus, critLevel=4)
		output = net.loop(steps=5000)
		output = filter(lambda x: len(x) > 1, output)
		print output
