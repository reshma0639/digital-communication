#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

maxpoints=30
max=3.0
min=-1.0
x = np.linspace(min,max,maxpoints)#points on the x axis
simlen = int(1e6)              #number of samples
cdf = []                       #declaring probability list
pdf = []                       #declaring pdf list
h = 2*max/(maxpoints-1);
randvar = np.loadtxt('uni1.dat',dtype='double') + np.loadtxt('uni2.dat',dtype='double')

for i in range(0,maxpoints):
	cdf_ind = np.nonzero(randvar < x[i])     #checking probability condition
	cdf_n = np.size(cdf_ind)                 #computing the probability
	cdf.append(cdf_n/simlen)                 #storing the probability values in a list

pdf = np.gradient(cdf, x, edge_order=2)

vec_tri_pdf = np.piecewise(x, [x < 0, ((x >= 0) & (x < 1)), ((x >= 1) & (x < 2)), x >= 2], [0, lambda x: x, lambda x: 2-x, 0])
vec_tri_cdf = np.piecewise(x, [x < 0, ((x >= 0) & (x < 1)), ((x >= 1) & (x < 2)), x >= 2], [0, lambda x: x**2/2, lambda x: 2*x - x**2/2 - 1, 1])

plt.plot(x,cdf,'o')               # plotting estimated CDF
plt.plot(x,vec_tri_cdf)           # plotting theoretical CDF
plt.grid()                        #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

plt.savefig('2.4_cdf.pdf')
plt.savefig('2.4_cdf.png')

plt.show()
plt.close()

plt.plot(x,pdf,'o')              # plotting estimated PDF
plt.plot(x,vec_tri_pdf)          # plotting theoretical PDF
plt.grid()                       #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('2.4_pdf.pdf')
plt.savefig('2.4_pdf.png')

plt.show()

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter2/tri_cdf.pdf"))
#subprocess.run(shlex.split("termux-open ../../figs/chapter2/tri_pdf.pdf"))
#else
#plt.show() #opening the plot window
