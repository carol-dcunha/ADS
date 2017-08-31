import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
subjects=['Maths','Physics','Chemistry','Biology']
num = np.arange(len(subjects))
means_frank = (90, 55, 40, 65)
means_guido = (85, 62, 54, 20)
width=0.35

a=plt.bar(num,means_frank,width,label='Frank',color='g',alpha=0.3)
b=plt.bar(num+width,means_guido,width,label='Guido',color='b',alpha=0.3)

plt.xticks(num+width/2,subjects)
plt.ylabel('Marks')
plt.ylim(0,100)
plt.title("Marks obtained by Frank and Guido")
plt.legend()

plt.show()