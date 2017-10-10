import maxheap as mh

def testHeapOperations():
	lst=[10,20,50,60,35,25,90,75,5]
	obj=mh.MaxHeap(lst)
	assert(obj.getMaximum()==90)
	obj.testHeapOrder()
	obj.addElement(100)
	obj.testHeapOrder()
	assert(obj.removeMaximum()==100)
	assert(obj.getMaximum()==90)
	obj.testHeapOrder()


if __name__=="__main__":
	testHeapOperations()