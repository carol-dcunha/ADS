import numpy as np

print "numpy version:",np.__version__
print "\nnumpy configuration"
np.show_config()

arr1=np.zeros(10)
print "\nNull vector of size 10"
print arr1

arr1[4]=1
print "\nChange 5th element of the null vector"
print arr1

arr2=np.arange(10,50)
print "\nVector with values from 10 to 49"
print arr2

print "\nReversing the above vector"
arr3=arr2[::-1]
print arr3

print "\nCreating random vector and sorting it"
arr4=np.random.random(10)
arr4.sort()
print arr4


arr5=np.arange(0,10,2)
print "\n",arr5
print "Negate elements between 3 and 8"
arr5[(3 < arr5) & (arr5 < 8)] *= -1
print arr5

print "\n3X3 matrix with values ranging from 0 to 8"
arr6 = np.arange(9).reshape(3,3)
print arr6

print "\nNon zero elements in [1,2,0,0,4,0]"
#nz=np.nonzero([1,2,0,0,4,0])
arr7=np.array([1,2,0,0,4,0])
print arr7[(arr7 != 0)]

print "\n3X3 identity matrix"
arr8=np.eye(3)
print arr8

print "\n3X3X3 matrix with random values"
arr9=np.random.random((3,3,3))
print arr9

A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.allclose(A,B)
print "\nA=",A,"\nB=",B
print "A==B?",equal

arr10=np.random.random(30)
print "\nMean=",arr10.mean()

arr11=np.random.random(10)
print "\n",arr11
arr11[arr11.argmax()]=0
print "Replacing maximum element\n",arr11

arr12 = np.random.randint(0,10,50)
print "\n",arr12
print "Frequently occuring element",
print(np.bincount(arr12).argmax())

arr13 = np.arange(10000)
np.random.shuffle(arr13)
n = 5
print "\nFirst 5 maximum elements"
# Slow
print "argsort method:",(arr13[np.argsort(arr13)[-n:]])

# Fast
print "argpartition method:",(arr13[np.argpartition(-arr13,n)[:n]])