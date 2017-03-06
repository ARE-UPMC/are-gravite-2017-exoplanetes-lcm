# -*- coding: utf-8 -*-
"""
Created on Lundi 06 Mars 2017 - ARE - 

@author: BOUKHALFI MOURAD 3679709
"""

import numpy as np
import matplotlib.pyplot as plt

circle1 = plt.Circle((0, 0), 0.01, color="yellow")
fig, ax = plt.subplots()
ax.add_artist(circle1)
fig.savefig('plotcircles.png')
#Tracer des cercles#
theta = np.linspace(0, 2*np.pi, 60)
#Orbite1#
x = np.cos(theta)
y = np.sin(theta)
#Orbite2#
x1 = np.cos(theta)
y1 = np.sin(theta)+0.1
#Orbite3#
x2 = np.cos(theta)
y2 = np.sin(theta)+0.2

#Affichage de toute les orbites#
plt.plot(x, y,x1,y1,x2,y2,color="black")


plt.show()
