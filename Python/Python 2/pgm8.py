import classes.doublestackqueue as dsq

def test_queueoperations():
	que=dsq.DoubleStackQueue()
	que.enqueue(10)
	que.enqueue("Hello World")
	que.enqueue("Welcome")
	assert(que.length()==3)
	assert(que.dequeue()!="Hello World")
	assert(que.dequeue()=="Hello World")
	assert(que.length()==1)
	assert(que.dequeue()=="Welcome")

if __name__=="__main__":
	test_queueoperations()

