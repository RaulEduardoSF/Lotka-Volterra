#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:10:01 2022

@author: raul
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['seaborn-dark'])
font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size' : 16,
        }

def par():
    a = 50
    k = 1
    return [a, k]

def RK4(y, t, h):
    """Runge-Kutta 4 method"""
    k1 = h*f(y, t)
    k2 = h*f(y+k1/2, t+h/2)
    k3 = h*f(y+k2, t+h/2)
    k4 = h*f(y+k3, t+h)
    return (k1 + 2*k2 + 2*k3 + k4)/6

def f(y, t):
    v = par()
    Pobl = y
    dotP = v[0]*Pobl*(1 - Pobl/v[1])
    return dotP

h = 1.0e-3
tstep = np.arange(0, 1, 0.5)
Pstep = []
p0 = 1

r = p0
for t in tstep:
    Pstep.append(r)
    r += RK4(r, t, h)

v = par()

plt.figure(dpi = 150, figsize = (7,5))
plt.xlabel("tiempo")
plt.ylabel("población")
plt.title("a = {}, kp = {}". format(v[0],v[1]))

plt.scatter(tstep[0], Pstep[0], label="$P_0$ = {}". format(p0))
plt.plot(tstep, Pstep)

plt.legend(title="Valores iniciales")
plt.show()