
#legendre polynomial
#(7) g(x,t) = (1-2*x*t+t**2)**(-0.5) = sum(0-->inf)(P(n,x)*t**(n))

import numpy as np
from scipy.special import legendre
from scipy.misc import derivative
x=float(input("enter the x: "))
t=float(input("Enter the t: "))
n=0
LHS=(1-2*x*t+t**2)**(-0.5)
term=(legendre(n)(x))*t**(n)
RHS=term
s=0.0
while(abs(term)>1.0e-8):
    term=(legendre(n)(x))*t**(n)
    s=s+term
    R=s
    n=n+1


print("LHS: ",LHS)
print("RHS: ",RHS)


