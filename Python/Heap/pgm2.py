import maxheap as mh

def testHeapOperations():
	lst=[10,20,50,60,35,25,90,75,5]
	obj=mh.MaxHeap(lst)
	obj.heapSort()
	obj.testSort()


if __name__=="__main__":
	testHeapOperations()