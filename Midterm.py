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
Positiony=Anavel*burn_time
print Anavel
Positiony=Anavel*burn_time

# Graph equations

dt=000000000001
<<<<<<< HEAD
t=np.linspace(1,burn_time-dt, 10000)
Ft_thrust=F_thrust*np.linspace(1,1,10000)
VAna=Exhaust_vel*np.log((Empty_mass+Max_fuel)/(Empty_mass-(burn_rate*t)))
velT=Ft_thrust/delmass*burn_time
ypost=VAna*t
=======
t=np.linspace(0,burn_time-dt, 10000)
ypost=Anavel*t
Ft_thrust=F_thrust*np.linspace(1,1,10000)
VAna=Exhaust_vel*np.log((Empty_mass+Max_fuel)/(Empty_mass-(burn_rate*t)))
velT=delMom/delmass*t
>>>>>>> origin/master

# Gravity
gs=9.8
Rade=6.37*10**6
g=gs/(1+(Positiony/Rade))**2
print g
gt=gs/(1+ypost/Rade)**2
<<<<<<< HEAD
Vana2=VAna-gs*t
# Air resistance
Temp_Lapse = 0.0065
Press_Sea = 1.01 * 10 ** 5
Molar_mass = 0.02896
Ideal_Gas = 8.314
Sea_press=1.01*10**5
T=288-ypost*Temp_Lapse
Pressure=Sea_press*(T/288.0)**(gt*Molar_mass/(Ideal_Gas* Temp_Lapse))
Forced=.5*Pressure*Area*drag_co*(Vana2)**2
=======

VAna2=VAna-gs*t
>>>>>>> origin/master

#Air Resistence

Anavel2=VAna-gs*t
# Air resistance
VAna2=VAna-gs*t
# Plots for position, velocity(Analytical and not), and force with respect to time

#Force

plt.subplot(3,1,1)
plt.plot(t,Forced,"g")
plt.plot(t,Ft_thrust,"b")
plt.plot(t,gt,"r")
plt.title("Force [N] vs. Time [s]")
plt.ylabel("N")

#velocity
plt.subplot(3,1,2)
plt.plot(t,velT,"b")
plt.plot(t,VAna, "r")
<<<<<<< HEAD
plt.plot(t,Vana2,"k")
=======
plt.plot(t,VAna2,"k")
>>>>>>> origin/master
plt.title("Velocity [m/s] vs. Time [s]")
plt.ylabel("[m/s]")

#position
print Positiony
plt.subplot(3,1,3)
plt.plot(t,ypost,"y")
plt.title("Height [m/s] vs Time [s]")
plt.ylabel("m")
plt.show()




