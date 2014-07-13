import numpy.random as npr
import sys
import numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def bak_update(sand):
	sand[npr.randint(0, 100)][npr.randint(0,100)] += 1
	for i in xrange(100):
		for j in xrange(100):
			if (sand[i][j] >= 4):
				sand[i][j] -= 4 #don't set equal to 0, subtract by 4
				if i < 99:
					sand[i+1][j] += 1
				if i > 1:
					sand[i-1][j] += 1
				if j < 99:
					sand[i][j+1] += 1
				if j > 1:
					sand[i][j-1] += 1

def bak_model():
	sand = numpy.zeros((100, 100), dtype=numpy.uint8)
	for i in range(10000):
		if i % 50 == 0:
			print "i: ", i
		bak_update(sand)
	#now show it
	plt.figure()
	plt.imshow(sand)
	plt.show()

if __name__ == "__main__":
	bak_model()
