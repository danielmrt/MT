# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 15:22:04 2014

@author: danie_000
"""
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
def a(t):
    