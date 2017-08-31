import classes.circularqueue as cq

def test_rotatequeue():
	que=cq.CircularQueue()
	que.enqueue(10)
	que.enqueue("Hello World")
	que.enqueue("Welcome")	
	assert(que.length()==3)
	
	que.rotate()
	assert(que.dequeue()=="Hello World")
	
	que.rotate()
	que.enqueue("Bye")
	assert(que.firstElement()==10)
	assert(que.lastElement()=="Bye")
	
	que.rotate()
	assert(que.firstElement()=="Welcome")
	assert(que.lastElement()==10)

	
if __name__=="__main__":
	test_rotatequeue()

