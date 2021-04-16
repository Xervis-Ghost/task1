import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as fsolve
##define your function as 2x^2+5
def f(x):
    return x**3 + 1
def bisection(a,b,tol):
    
    xr=a
    xl=b
    while (np.abs(xr-xl)>=tol):
        c=(xl+xr)/2
        prod= f(c)*f(xl)
        if prod >tol:
            xl=c
                
        else:
            if prod <tol:
               xr=c
    return c
answer= bisection(-5,5,1e-8)
print (answer)
        
x=np.linspace(-2,2,100)
plt.plot(x,f(x))
plt.grid()
plt.show()
