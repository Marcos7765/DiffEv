#test functions
import numpy as np
#ackley

f64_5 = np.float64(5)
limits = [(-f64_5, f64_5), (-f64_5, f64_5)]
popSize = 10
maxGen = 100
mf = 0.5
CR = 0.1
maximize = False
fobj = lambda x : 20+ np.e - 20*np.exp(-0.2 * np.sqrt((x[0]**2 + x[1]**2)/2)) - np.exp((np.cos(2*np.pi*x[0]) + np.cos(2*np.pi*x[1]))/2 )

# another one
'''
a = 500
b = 0.1
c = np.pi/2
x1 = lambda x : 25*x
x2 = lambda y : 25*y
F10 = lambda x : -a * np.exp(-b * np.sqrt( (x1(x[0])**2 + x2(x[1])**2) /2) ) - \
    np.exp((np.cos(c*x1(x[0])) + np.cos(c*x2(x[1]))) /2) + np.exp(1)
zsh = lambda x : 0.5 - (( np.sin( np.sqrt(x[0]**2 + x[1]**2) )**2 ) -0.5)/ \
    ((1 + 0.1* (x[0]**2 + x[1]**2) )**2)
Fobj = lambda x : F10(x)*zsh(x)
r = lambda x : 100*(x[1] - x[0]*x[0])**2 + (1 - x[0])**2
rd = lambda x : 1 + (x[1] - x[0]**2)**2 + (1-x[0])**2
z = lambda x : x[0]*np.sin(np.sqrt(abs(x[0]))) - x[1]*np.sin(np.sqrt(abs(x[1])))
w4 = lambda x : np.sqrt(r(x)**2 + z(x)**2)+Fobj(x)
w23 = lambda x : z(x)/rd(x)
w27 = lambda x : w4(x) + w23(x)
fobj = w27
'''