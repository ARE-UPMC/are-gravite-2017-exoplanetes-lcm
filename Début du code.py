# -*- coding: utf-8 -*-
"""
Created on Lundi 06 Mars 2017 - ARE - 

@author: BOUKHALFI MOURAD 3679709
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

circle1 = plt.Circle((0, 0), 0.3, color="yellow")
fig= plt.figure()
fig.set_dpi(100)
fig.set_size_inches(10, 10)



ax=plt.axes(xlim=(-4, 4), ylim=(-4, 4))
ax.add_artist(circle1)
#Tracer des cercles#
theta = np.linspace(0, 2*np.pi, 60)
#Orbite1#
x = 2* np.cos(theta)
y = 2* np.sin(theta)
#Orbite2#
x1 =  3* np.cos(theta)
y1 = 3* np.sin(theta)
#Orbite3#
x2 = np.cos(theta)
y2 = np.sin(theta)

#Affichage de toute les orbites#
plt.plot(x, y,x1,y1,x2,y2,color="black")

size = 0.2
xcenter = 0
ycenter = 0
radius = 3



size2 = 0.1
radius2=2

patch = plt.Circle((5,-5), size, fc='b')
patch2 = plt.Circle((3, -3), size2, fc='r')

def init():
    patch.center = (xcenter, ycenter)
    patch2.center = (xcenter, ycenter)
    ax.add_patch(patch)
    ax.add_patch(patch2)
    return patch, patch2,

def animate(t):
    x,y = patch.center
    x = xcenter + radius * np.sin(np.radians(t))
    y = ycenter + radius * np.cos(np.radians(t))
    patch.center = (x,y)
    x,y = patch2.center
    x = xcenter + radius2 * np.sin(np.radians(t))
    y = ycenter + radius2 * np.cos(np.radians(t))
    patch2.center= (x,y)
    
    return patch, patch2,



anim = animation.FuncAnimation(fig, animate, init_func=init, frames=300, interval=20, blit=True)

plt.show()
