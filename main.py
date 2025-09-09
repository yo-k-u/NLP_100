import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-6,6,1)
y=1/(1+np.exp(-x))
plt.plot(x,y)
plt.show()