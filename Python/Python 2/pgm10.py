import classes.limitedstack as ls
import classes.circularqueue as cq

def findElement(stk,key):

	que=cq.CircularQueue()
	status=False
	datalist=[]
	for i in range(stk.length()):
		item=stk.pop()
		if item==key:
			status=True
		que.enqueue(item)
	for i in range(que.length()):
		datalist.append(que.dequeue())
	for item in range(len(datalist)):
		stk.push(datalist.pop())
	return status


def test_findelement():
	stk=ls.LimitedStack()
	stk.push(10)
	stk.push(20)
	stk.push("Hello")
	stk.push("World")
	stk.push("Python")
	stk.push("Element")
	stk.push(30)

	assert(findElement(stk,20)==True)
	assert(findElement(stk,"Element")==True)
	assert(findElement(stk,32.0)==False)
	assert(stk.peak()==30)
	assert(stk.length()==7)

if __name__=="__main__":
	test_findelement()