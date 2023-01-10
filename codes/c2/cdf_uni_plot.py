#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if



x = np.linspace(-4,4,30)  #points on the x axis
simlen = int(1e6)         #number of samples
err = []                  #declaring probability list
randvar = np.loadtxt('uni.dat',dtype='double')

for i in range(0,30):
	      err_ind = np.nonzero(randvar < x[i])   #checking probability condition
	      err_n = np.size(err_ind)               #computing the probability
	      err.append(err_n/simlen)               #storing the probability values in a list

	
plt.plot(x.T,err)        #plotting the CDF
plt.grid()               #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')


plt.savefig('cdf_uni.png')
plt.savefig('cdf_uni.pdf')

#if using termux
#subprocess.run(shlex.split("termux-open ../fig/c2/cdf_uni.pdf"))

plt.show()       #opening the plot window
