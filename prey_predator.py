#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:25:26 2022

@author: Raul Santoy
Modelo Presa Depredador
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['seaborn-dark'])
font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size' : 16,
        }

def RK4(r, t, h):
    """Runge-Kutta 4 method"""
    k1 = h*f(r, t)
    k2 = h*f(r+k1/2, t+h/2)
    k3 = h*f(r+k2, t+h/2)
    k4 = h*f(r+k3, t+h)
    return (k1 + 2*k2 + 2*k3 + k4)/6

def par():
    a = 4
    b = 0.9
    c = 0.16
    d = 0.08
    kp= 2.5
    kd= 0.5
    return np.array([a, b, c, d, kp, kd])

def punto():
    v = par()
    x = v[2]/v[3]
    y = v[0]/v[1]*(1 - v[2]/(v[3]*v[4]))
    return (x, y)

def f(r, t):
    v = par()
    P = r[0]
    D = r[1]
    #dotP = v[0]*(1 - P/v[4])*P - v[1]*D*P
    dotP = (v[0] - v[1]*D)*P
    dotD = (-v[2] + v[3]*P)*D
    #dotD = -v[2]*(1 - D/v[5])*D + v[3]*D*P
    return np.array([dotP,dotD], float)

h = 1.0e-3
tstep = np.arange(0, 500, 0.01)
Pstep, Dstep = [], []
p0 = 10
d0 = 6

r = np.array([p0, d0], float)    
for t in tstep:
    Pstep.append(r[0])
    Dstep.append(r[1])    
    r += RK4(r, t, h)

v = par()

beta = 1 + np.sqrt(1 + v[0]/v[2])
p1 = 1/v[4]
p2 = 2*(v[3]/v[2])/beta
p3 = v[3]/v[2]

print("1/k_p = {:.4f}". format(p1))
print("2(d/c)/beta = {:.4f}". format(p2))
print("d/c = {:.4f}". format(p3))

if (2*(v[3]/v[2])/beta < 1/v[4] < v[3]/v[2]):
    print("Atractor/Espiral Out", punto())    
    print("P/D = {:.4f}". format(Pstep[-1]/Dstep[-1]))


if (1/v[4] < 2*(v[3]/v[2])/beta):
    print("Punto Silla/Espiral_IN", punto())
    print("P/D = {:.4f}". format(Pstep[-1]/Dstep[-1]))


plt.figure(dpi = 150, figsize = (7,5))
plt.xlabel("tiempo")
plt.ylabel("población")
plt.scatter(tstep[0], Dstep[0], label="$D_0$ = {}". format(d0))
plt.scatter(tstep[0], Pstep[0], label="$P_0$ = {}". format(p0))
#plt.scatter(tstep[-1], Dstep[-1], label="$D_f$ = {:.4f}". format(Dstep[-1]))
#plt.scatter(tstep[-1], Pstep[-1], label="$P_f$ = {:.4f}". format(Pstep[-1]))
plt.title("a = {}, b = {}, c = {}, d = {}, kp = {}". format(v[0],v[1],v[2],v[3],v[4]))
plt.plot(tstep, Dstep)
plt.plot(tstep, Pstep)
plt.legend(title="Valores iniciales")
#plt.savefig("e"+name+"_p{}-d{}.png". format(p0, d0))
plt.show()

plt.figure(dpi = 150, figsize = (7,5))
plt.title("a = {}, b = {}, c = {}, d = {}, kp = {}". format(v[0],v[1],v[2],v[3],v[4]))
plt.scatter(p0,d0, label="$P_0={}$, $D_0={}$". format(p0,d0))
plt.scatter(Pstep[-1], Dstep[-1], label=" $P_f$ = {:.2f}, $D_f$ = {:.2f}". format(Pstep[-1], Dstep[-1]))
#plt.scatter(punto()[0], punto()[1], label="$Pc = ({:.2f},{:.2f})$". format(punto()[0], punto()[1]))
plt.plot(Pstep,Dstep)
plt.xlabel("Prey")
plt.ylabel("Predator")
plt.legend()
#plt.savefig("f"+name+"_p{}-d{}.png". format(p0, d0))
plt.show()

