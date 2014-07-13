import numpy
import scipy.ndimage

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot

def vfunc(conv, rand, p=0.05, f=0.005):
	#tree + neighbor on fire = burning
	if conv >= 110:
		return 10
	#no tree, check for new tree
	if conv < 100:
		if rand < p:
			return 1
		else:
			return 0
	#ow., check for fire
	if rand < f:
		return 10
	else:
		return 1

update_func = numpy.vectorize(vfunc, [numpy.int8])

class Forest(object):
	"""
	Bak-Chen-Tang forest fire model
	n: num of rows and columns
	"""
	def __init__(self, n, mode='wrap'):
		self.n = n
		self.mode = mode
		self.array = numpy.zeros((n, n), numpy.int8)
		self.weights = numpy.array([[1,1,1],[1,100,1],[1,1,1]])

	def get_array(self, start=0, end=None):
		if start==0 and end==None:
			return self.array
		else:
			return self.array[:, start:end]

	def loop(self, steps=1):
		[self.step() for i in xrange(steps)]

	def step(self):
		con = scipy.ndimage.filters.convolve(self.array, self.weights, mode=self.mode)
		rand = numpy.random.rand(self.n, self.n)
		self.array = update_func(con, rand)

	def count(self):
		data = []
		a = numpy.int8(self.array == 1) #the number of trees
		for i in range(self.n):
			total = numpy.sum(a[:i, :i])
			data.append((i+1, total))
		return zip(*data)

class ForestViewer(object):
	def __init__(self, forest, cmap=matplotlib.cm.gray_r):
		self.forest = forest
		self.cmap = cmap
		self.fig = pyplot.figure()
		pyplot.axis([0, forest.n, 0, forest.n])
		pyplot.xticks([])
		pyplot.yticks([])
		self.pcolor = None
		self.update()

	def update(self):
		if self.pcolor:
			self.pcolor.remove()
		a = self.forest.array
		self.pcolor = pyplot.pcolor(a, vmax=10, cmap=self.cmap)
		self.fig.canvas.draw()

	def animate(self, steps=10):
		self.steps = steps
		self.fig.canvas.manager.window.after(1000, self.animate_callback)
		pyplot.show()

	def animate_callback(self):
		for i in range(self.steps):
			self.forest.step()
			self.update()

if __name__ == '__main__':
	forest = Forest(50)
	viewer = ForestViewer(forest)
	viewer.animate(100)
