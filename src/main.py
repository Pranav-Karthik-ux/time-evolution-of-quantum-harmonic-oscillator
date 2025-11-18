#time evolution of a harmonic oscillator
from scipy import special
from qutip import *
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def psi_n(n,x,x0):
    y=x/x0
    t=1/np.sqrt(math.factorial(n)*2**(n)*x0*np.sqrt(np.pi))
    H=special.hermite(n,monic=False)
    return( t*H(y)*np.exp(-(y**2/2)))

def time_evolution(n,t,x,x0,w):
    y=np.exp(-1j*(n+0.5)*w*t)*psi_n(n,x,x0)
    return y
 
def psi(l,x,x0,t,w):
    y=0+0j
    f=0
    for i in range(len(l)):
        y+=l[i]*time_evolution(i,t,x,x0,w)
        f+=l[i]**2
    return y/f

l=[1,0,3,7] # of the form l[0]|0⟩+l[1]|1⟩... it is normalized in the psi function
dt=0.25
t=np.arange(0,200,0.5)

w=0.2
m=9.1*10**(-31)
x0=np.sqrt(1.03*10**(-34)/(m*w))
x=np.linspace(-5*x0,5*x0,1000)
fig,ax= plt.subplots(2,1)
line, = ax[0].plot(x,np.real(psi(l,x,x0,0,w)))
line2, = ax[1].plot(x,np.imag(psi(l,x,x0,0,w)))
ax[0].set_ylim(-max(np.real(psi(l,x,x0,0,w))),max(np.real(psi(l,x,x0,0,w))))
ax[0].set_xlabel('x')
ax[0].set_ylabel('real \u03C8')
ax[1].set_ylim(-max(np.real(psi(l,x,x0,0,w))),max(np.real(psi(l,x,x0,0,w))))
ax[1].set_xlabel('x')
ax[1].set_ylabel('imaginary \u03C8')
def update(t):
    y=np.real(psi(l,x,x0,t,w))
    y2=np.imag(psi(l,x,x0,t,w))
    line.set_ydata(y)
    line2.set_ydata(y2)
    return line, line2,
ani = FuncAnimation(fig, update, frames=t, interval=50, blit=True)

plt.show()
