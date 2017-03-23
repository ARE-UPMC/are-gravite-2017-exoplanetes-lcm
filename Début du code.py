# -*- coding: utf-8 -*-
"""
Created on Lundi 06 Mars 2017 - ARE - 

@author: BOUKHALFI MOURAD 3679709 CARTON LORRIS 3521310
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation




#Creation des cercles representant le centre de masse et la terre#
circle1 = plt.Circle((0, 0), 0.3, color="red", label="Centre de masse")
circle2 = plt.Circle((0,-3.9), 0.2, color="blue", label="Terre (Observateur)")

#Initialisation de la figure#
fig= plt.figure("Representation de l'exoplanète hd189533b ayant une periode de rotation de 2,2 jours terrestres", facecolor="white")
fig.set_dpi(95)
fig.set_size_inches(50, 50)
ax=plt.axes(xlim=(-4, 4), ylim=(-4, 4))
plt.axis('equal')
plt.axis('off')#Effacement des axes
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())#Ouverture de la fenetre en Taille grande#


ax.add_artist(circle1)
ax.add_artist(circle2)
#Tracer des cercles#
theta = np.linspace(0, 2*np.pi, 60)

#Orbite1#
x1 =  3* np.cos(theta)
y1 = 3* np.sin(theta)
#Orbite2#
x2 = np.cos(theta)
y2 = np.sin(theta)

#Affichage des orbites#
plt.plot(x1,y1,x2,y2,color="black")

#Affichage de la ligne de visée#
plt.plot([0.2,0.2],[-4,4], color="green")
plt.plot([-0.2,-0.2],[-4,4], color="green")

#Affichage de la distance Terre- Exoplanete dans une legende differente#
distance= plt.arrow(0,-3.7,0,0.6, head_width= 0.05, head_length= 0.1, fc='m', ec='m', label="(fleche) 60 années lumiere = distance Terre/Exoplanete")
first_legend = plt.legend(handles=[distance], loc="lower left")
ax.add_artist(first_legend)


#Variables de l'exoplanète#                  
size = 0.1
xcenter = 0
ycenter = 0
radius = 3


#Variables du Soleil#
size2 = 0.3
radius2=1

#Creation des Patchs#
patch = plt.Circle((5,-5), size, fc='black', label="Exoplanete (hd189533b)")
patch2 = plt.Circle((0, -2), size2, fc='yellow', label="Soleil")
patch3=plt.arrow(0,3,1, 0, head_width=0.05, head_length=0.1, fc="purple", ec="purple", label="(fleche) sens du Soleil")
patch4=plt.arrow(0,-1,-1,0, head_width=0.05, head_length=0.1, fc="orange", ec="orange", label="(fleche) sens de l'exoplanete")

#Fonction qui initialise l'animation#
def init():
    patch.center = (xcenter, ycenter)
    patch2.center = (xcenter, ycenter)
    ax.add_patch(patch)
    ax.add_patch(patch2)


    return patch, patch2,patch3,patch4,

#Fonction qui anime le Soleil et l'exoplanète#
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


#Affichage de la lègende en boite au dessus de la figure#

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,ncol=2, mode="expand", borderaxespad=0, handles=[circle1, patch, patch2, circle2, patch3, patch4])

#Appel de la fonction animation#
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1000000, interval=20, blit=True)

#Affichage final#

plt.show()
