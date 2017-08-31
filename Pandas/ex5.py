import numpy as np 
import matplotlib.pyplot as plt 

x=np.arange(0,20,1)
y1=np.arange(5,101,5)
y2=np.arange(10,201,10)
y3=np.arange(15,301,10)

plt.subplot(2,2,1)
plt.plot(x,y1,label="line1",marker='o',lw=2,color='g')
plt.legend()

plt.subplot(2,2,2)
plt.plot(x,y2,label="line2",marker='o',lw=2,color='b',linestyle="dashed")
plt.legend()

plt.subplot(2,1,2)
plt.plot(x,y2,label="line3",marker='o',lw=2,color='r')
plt.legend()

plt.show()