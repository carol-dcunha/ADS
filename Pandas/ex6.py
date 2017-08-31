import numpy as np 
import matplotlib.pyplot as plt 

objects=("Pyhton","C++","Java","Perl","Scala","Lisp")
y_pos=np.arange(len(objects))
performance=[8,6,4,3,2,1]

plt.bar(y_pos,performance,align='center',alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel("Performance")
plt.title("Programming Language Usage")
plt.show()