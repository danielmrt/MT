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
delmass=Empty_mass

burn_time=Max_fuel/burn_rate #aka delta t
delMom=burn_rate*burn_time*Exhaust_vel #AKA delta P
F_thrust=delMom/burn_time

Anavel=Exhaust_vel*np.log((Empty_mass+Max_fuel)/Empty_mass)
<<<<<<< HEAD
print Anavel
Positiony=Anavel*burn_time
=======

>>>>>>> origin/master

# Graph equations

dt=000000000001
t=np.linspace(1,burn_time-dt, 10000)


Ft_thrust=F_thrust*np.linspace(1,1,10000)
VAna=Exhaust_vel*np.log((Empty_mass+Max_fuel)/(Empty_mass-(burn_rate*t)))
velT=delMom/(delmass*t)
ypost=VAna*t
# Gravity
gs=9.81
Rade=6.37*10**6
gt=gs/(1+ypost/Rade)**2
<<<<<<< HEAD
VAna2=VAna-gs*t

#Air Resistence
=======
Anavel2=VAna-gs*t
# Air resistance

>>>>>>> origin/master


# Plots for position, velocity(Analytical and not), and force with respect to time

#Force

plt.subplot(3,1,1)
plt.plot(t,Ft_thrust,"b")
plt.plot(t,gt,"r")
plt.title("Force [N] vs. Time [s]")
plt.ylabel("N")

#velocity
plt.subplot(3,1,2)
plt.plot(t,velT,"b")
plt.plot(t,VAna, "r")
plt.plot(t,Anavel2,"k")
plt.title("Velocity [m/s] vs. Time [s]")
plt.ylabel("[m/s]")

#position

<<<<<<< HEAD
print Positiony
=======


>>>>>>> origin/master
plt.subplot(3,1,3)
plt.plot(t,ypost,"y")
plt.title("Height [m/s] vs Time [s]")
plt.ylabel("m")
plt.show()




