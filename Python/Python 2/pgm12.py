import classes.doubleendedqueue as deq

def test_queueoperations():
	que=deq.DoubleEndedQueueArray()
	que.addFirst(10)
	que.addFirst("Hello World")
	que.addLast("Python")
	assert(que.firstElement()=="Hello World")
	que.addLast("Welcome")
	assert(que.length()==4)	
	assert(que.lastElement()!="Hello World")
	que.addLast("Bye")
	assert(que.firstElement()=="Hello World")
	que.addLast("Lab")
	assert(que.firstElement()==10)
	assert(que.deleteFirst()==10)
	assert(que.length()==4)
	assert(que.deleteLast()=="Lab")
	assert(que.length()==3)


if __name__=="__main__":
	test_queueoperations()

