# -*- coding: utf-8 -*-
"""
Created on Lundi 06 Mars 2017 - ARE - 

@author: BOUKHALFI MOURAD 3679709 CARTON LORRIS 3521310
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


circle1 = plt.Circle((0, 0), 0.3, color="red", label="Centre de masse")
circle2 = plt.Circle((0,-3.9), 0.2, color="blue", label="Terre (Observateur)")
fig= plt.figure()
fig.set_dpi(100)
fig.set_size_inches(50, 50)



ax=plt.axes(xlim=(-4, 4), ylim=(-4, 4))

ax.add_artist(circle1)
ax.add_artist(circle2)
#Tracer des cercles#
theta = np.linspace(0, 2*np.pi, 60)

#Orbite2#
x1 =  3* np.cos(theta)
y1 = 3* np.sin(theta)
#Orbite3#
x2 = np.cos(theta)
y2 = np.sin(theta)

#Affichage des orbites#
plt.plot(x1,y1,x2,y2,color="black")
plt.plot([0.2,0.2],[-4,4], color="green")
plt.plot([-0.2,-0.2],[-4,4], color="green")

size = 0.1
xcenter = 0
ycenter = 0
radius = 3



size2 = 0.3
radius2=1

patch = plt.Circle((5,-5), size, fc='black', label="Exoplanete")
patch2 = plt.Circle((0, -2), size2, fc='yellow', label="Soleil")


def init():
    patch.center = (xcenter, ycenter)
    patch2.center = (xcenter, ycenter)
    ax.add_patch(patch)
    ax.add_patch(patch2)

    return patch, patch2,

def animate(t):
    x,y = patch.center
    x = xcenter + radius * np.cos(np.radians(t))
    y = ycenter  - radius * np.sin(np.radians(t))
    patch.center = (x,y)
    x,y = patch2.center
    x = xcenter - radius2 * np.cos(np.radians(t))
    y = -(ycenter - radius2 * np.sin(np.radians(t)))
    patch2.center= (x,y)
    
    return patch, patch2,



plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=2, mode="expand", borderaxespad=0, handles=[circle1, patch, patch2, circle2])

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1000000, interval=20, blit=True)


plt.show()
