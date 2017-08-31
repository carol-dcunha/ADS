import numpy as np 
import matplotlib.pyplot as plt 

x=np.arange(0,20,1)
y1=np.arange(5,101,5)
y2=np.arange(10,201,10)

plt.plot(x,y1,label="line1",marker='o',lw=2)
plt.plot(x,y2,label="line2",marker='o',lw=2)
plt.legend()

plt.show()