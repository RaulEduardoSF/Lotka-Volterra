#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:22:06 2022

@author: Raul Santoy
@title: Bifurcations to Prey Predator Model
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['seaborn-dark'])
font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size' : 16,
        }


def pp(a, kp):
    return np.array([a,kp], float)

def f(yy, u):
    a = u[0]
    k = u[1]
    P = yy
    dotP = a*P*(1 - P/k)
    return dotP

def evo(y, u):
    err = 1e-6
    tstep = np.arange(0, 75, 0.0001)
    Pobl = [y]
    for t in tstep:
        y = u[0]*y*(1-y)
        Pobl.append(y)
    return Pobl[-1]
    return min(Pobl), max(Pobl)

x = []
p = []
p0 = 0.6
k = 1

a0 = 1
af = 4

for a in np.arange(a0, af, 0.0005):
    u = pp(a, k)
    z = evo(p0, u)
    x.append(a)
    p.append(z)
    #x.append(a)
    #p.append(z[1])
    
plt.figure(dpi = 200, figsize = (7,5))
plt.xlabel("a")
plt.ylabel("Población estable")   
plt.title("$a = [{},{}]$, $k$ = {}, $p_0$ = {}". format(a0, af, k, p0))
plt.scatter(np.array(x), np.array(p), alpha=0.1 ,label = "k = {}". format(k))
#plt.scatter(x, p, alpha=0.25 ,label = "k = {}". format(k))
#plt.ylim(min(p),max(p))
plt.legend()
plt.show()
