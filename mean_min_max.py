import numpy
import matplotlib.pyplot
#Fixme : provide data file
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
#Change the size
fig = matplotlib.pyplot.figure(figsize=(10.0, 4.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('Average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('Max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('Min')
axes3.plot(numpy.min(data, axis=0))

fig.tight_layout()

matplotlib.pyplot.show()
