# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 15:22:04 2014

@author: danie_000
"""
import numpy as np
import matplotlib.pyplot as plt

#Initial Data
emp_mass = 10000
maxfuel_mass = 10000
exaust_v = 7000
burn_rate = 100
ref_area = 10
drag_co = 0.5
h_ISS = 355000
m_t= maxfuel_mass + emp_mass

#Rocket thrust
# F = ma //  F/m = a
# F = Thrust , by equation 6.7b F = burn rate * exaust velocity
# We are losing mass each second so ( - burn rate * t )
def a(t):
    return (burn_rate * exaust_v / (m_t - burn_rate*t))
start = 0.0
end = 100
N = 100000
h = (end-start)/float(N)
t_1= np.arange(start, end, h)
v1 = 0.0
h1 = 0.0
t1= 0.0
v1 = v1 - 0.5*h*a(t1)
v_1 = []
h_1 = []

for t in t_1:								
    if t <= 100.0:
        h_1.append(h1)
        v_p = v1 + 0.5*h*a(t)
        v_1.append(v_p)
        v1 += h*a(t)
        h1 += h*v1
    else:										
        h_1.append(h)
        v_1.append(v1)				
        h1 += h*v1
        
# height vs. time
plt.subplot(3,1,1)
plt.plot(t_1, h_1, label = 'height')
plt.legend(loc=2)
plt.show()
# velocity vs. time
plt.subplot(3,1,2)
plt.plot(t_1, v_1, label = 'velocity')
plt.legend(loc=2)
plt.show()
