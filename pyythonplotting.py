import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,10)
y = np.sin(x)

for i in range(8):
    plt.plot(x,y)
    plt.figure(i+1)

plt.show()
