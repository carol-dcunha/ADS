import classes.doubleendedqueue as deq

def test_queueoperations():
	que=deq.DoubleEndedQueue()
	que.addFirst(10)
	que.addFirst("Hello World")
	assert(que.firstElement()=="Hello World")
	que.addLast("Welcome")
	assert(que.length()==3)
	assert(que.lastElement()!="Hello World")
	que.addLast("Bye")
	assert(que.lastElement()=="Bye")
	assert(que.deleteFirst()=="Hello World")
	assert(que.length()==3)
	assert(que.deleteFirst()==10)
	assert(que.deleteLast()=="Bye")
	assert(que.length()==1)


if __name__=="__main__":
	test_queueoperations()

