import numpy as np
import matplotlib.pyplot as plt

maxlim = 20
maxpts = 50
x = np.linspace(-1, 20, 50)    #points on x-axis
simlen = int(1e6)              #number of samples
cdf = []                       #declaring probability list
uni_randvar = np.loadtxt('uni.dat',dtype='double')
V_randvar = -2*np.log(1-uni_randvar)

for i in range(0,maxpts):
	cdf_ind = np.nonzero(V_randvar < x[i])     #checking probability condition
	cdf_n = np.size(cdf_ind)                   #computing the probability
	cdf.append(cdf_n/simlen)                   #storing the probability values in a list


plt.plot(x, cdf)         #plotting CDF numerical 
plt.grid()
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')

plt.savefig('2.3.1_cdf.pdf')
plt.savefig('2.3.1_cdf.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter2/log_uni_cdf.pdf"))
#else
plt.show()
