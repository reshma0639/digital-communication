import numpy as np
import matplotlib.pyplot as plt

#if using termux
# import subprocess
#import shlex
# end if


maxpoints=100
max=10.0
x = np.linspace(0,max,maxpoints)           #points on the x axis
simlen = int(1e6)                          #number of samples
cdf = []                                   #declaring probability list
pdf = []                                   #declaring pdf list
h = 2*max/(maxpoints-1);
x1 = np.random.normal(0, 1, simlen)
x2 = np.random.normal(0, 1, simlen)
v = np.sqrt(x1**2 + x2**2)

for i in range(0,maxpoints):
	cdf_ind = np.nonzero(v < x[i])               #checking probability condition
	cdf_n = np.size(cdf_ind)                     #computing the probability
	cdf.append(cdf_n/simlen)                     #storing the probability values in a list
	
pdf = np.gradient(cdf, x, edge_order=2)

plt.plot(x.T,cdf)   #plotting the CDF
plt.grid()          #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.savefig('vroot_cdf.pdf')
plt.savefig('vroot_cdf.png')

plt.show()
plt.close()
	
plt.plot(x,pdf)             # plotting estimated PDF
plt.grid()                  #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')

plt.savefig('vroot_pdf.pdf')
plt.savefig('vroot_pdf.png')

plt.show()

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter4/chisq_cdf.pdf"))
#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter4/chisq_pdf.pdf"))
#else
#plt.show() #opening the plot window
