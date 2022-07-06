# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import math

def f(x):
    #return (2*x*x)+(9*x)-100
    return (x*x)-(2*x)-56

p0 = 0.7
tol = 0.0005
n0 = 10000

def Steffensen(f,p0,tol):
   
    for i in range(1,n0) :
        p1 = p0 + f(p0)
        p2 = p1 + f(p1)
        #print(pow((p2 - p1),2))
        print(p2 - (2*p1) + p0)
        p = p2 - (pow((p2 - p1),2)/(p2 - (2*p1) + p0))
        #print(p-p0)
        if abs(p-p0) < tol:
            print("Converge after %f iterations"%i)
            return p
        p0 = p
    print('failed to converge in %f iterations' %n0)
    return p

ans = Steffensen(f,p0,tol)
print("value is: %f"%ans)