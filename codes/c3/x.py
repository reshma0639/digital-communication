import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

samples = 1000
x = np.random.binomial(1,0.5,samples)*2-1
n = np.random.normal(0,1,samples)
A_DB = 5
A = 10**(0.1*A_DB)
y = A*x + n

x0 = np.extract(x==1, x)
x1 = np.extract(x==-1, x)
n0 = np.extract(x==1,n)
n1 = np.extract(x==-1, n)
y0 = A*x0 + n0
y1 = A*x1 + n1

plt.plot(y0, np.zeros(y0.shape[0]), 'o', mfc='none')
plt.plot(y1, np.zeros(y1.shape[0]), 'o', mfc='none')
plt.plot(np.zeros(10), np.linspace(-0.1,0.1,10), color="red")
plt.grid()
plt.legend(["$y|0$","$y|1$"])

plt.savefig('y_scatter.pdf')
plt.savefig('y_scatter.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter3/bpsk_scatter.pdf"))
#else
plt.show() #opening the plot window
