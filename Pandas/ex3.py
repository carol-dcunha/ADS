import numpy as numpy
import matplotlib.pyplot as plt

x=[20,30,40,50,60]
y=[12,78,23,12,50]

plt.plot(x,y,linestyle='dashed',color='g',marker='o',lw=2)
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.xticks(x,['x1','x2','x3','x4','x5'])
plt.title('Sample Graph')
plt.ylim(0,100)
plt.grid()
plt.show()

