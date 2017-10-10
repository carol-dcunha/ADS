import minheap as mh

def testHeapOperations():
	lst=[10,20,50,60,35,25,90,75,5]
	obj=mh.MinHeap(lst)
	assert(obj.getMinimum()==5)
	obj.testHeapOrder()
	obj.addElement(2)
	obj.testHeapOrder()
	assert(obj.removeMinimum()==2)
	assert(obj.getMinimum()==5)
	obj.testHeapOrder()
	obj.heapSort()
	obj.testSort()


if __name__=="__main__":
	testHeapOperations()