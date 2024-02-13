import numpy as np

from scipy.integrate import odeint

import matplotlib.pyplot as plt
 
def model(y,x):
    dydx = 2*np.cos(2*x) - np.sin(x)
    return dydx

y0 = 0
t = np.linspace(0,10,21)
y = odeint(model,y0 , t)
plt.plot(t,y,'ok')
xe = np.linspace(0,10,201)
ye = np.sin(2*xe)+np.cos(xe) -1
plt.plot(xe,ye,'k')
plt.xlabel('x') ; plt.ylabel('y(x)')
plt.title('Solutions of dy/dx = 2*cos(2*x) - sin(x)')
plt.show()