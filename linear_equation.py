from sympy import Eq, solve_linear_system, Matrix
from numpy import linalg
import numpy as np
import sympy as sp


print("Using Simpy:")

eq1=sp.Function("eq1")
eq2=sp.Function("eq2")

x,y=sp.symbols('x y')

eq1= Eq(2*x-y,6) #two valriable linear equation 
eq2= Eq(x-y,2) #two valriable linear equation 

display(eq1)
display(eq2)

row1=[2, -1, 6] #coefficients of x and y and the constant respectively
row2=[1, -1, 2] #coefficients of x and y and the constant respectively

system=Matrix((row1,row2))

display(system) #visualise the Matrix

display(solve_linear_system(system,x,y)) #main processing 
