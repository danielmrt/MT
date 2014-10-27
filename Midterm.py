# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 14:54:21 2014

@author: Chris
"""
import numpy as np
import matplotlib.pyplot as plt
#Initial conditions.
#The properties of this specific rocket. 
Empty_mass=10000.
Max_fuel=10000.
Exhaust_vel=7000.
burn_rate=100.
Area=10.
drag_co=.5

##Finding The forces using the above
# These come from values regarding thrust
delmass=Max_fuel
burn_time=Max_fuel/burn_rate #aka delta t
delMom=burn_rate*burn_time*Exhaust_vel #AKA delta P
F_thrust=delMom/burn_time
Anavel=Exhaust_vel*np.log((Empty_mass+Max_fuel)/Empty_mass)
print Anavel
# Gravity

 
# Plots for position, velocity(Analytical and not), and force with respect to time
dt=000000000001
t=np.linspace(0,burn_time-dt, 10000)
#Force
Ft_thrust=F_thrust*np.linspace(1,1,10000)
plt.plot(t,Ft_thrust,"g")
plt.title("Force vs. Time")
plt.xlabel("time")
plt.ylabel("Force")
plt.show()
#velocity
VAna=Exhaust_vel*np.log((Empty_mass+Max_fuel)/(Empty_mass-(burn_rate*t)))
velT=delMom/delmass*t
plt.plot(t,velT,"b")
plt.plot(t,VAna, "r")
plt.title("Velocity vs. Time")
plt.xlabel("time in seconds")
plt.ylabel("Velocity in m/s")
plt.show()
#position
Positiony=Anavel*burn_time
ypost=Anavel*t
print Positiony
plt.plot(t,ypost,"y")
plt.title("Height vs Time")
plt.xlabel("Time")
plt.ylabel("Height")
plt.show()


