import classes.singlequeuestack as sqs

def test_stackoperations():
	stk=sqs.SingleQueueStack()
	stk.push(10)
	stk.push("Hello World")
	stk.push("Welcome")
	assert(stk.peak()=="Welcome")
	assert(stk.length()==3)
	assert(stk.pop()!="Hello World")
	assert(stk.length()==2)
	assert(stk.pop()=="Hello World")
	assert(stk.peak()==10)
	assert(stk.pop()==10)
	assert(stk.length()==0)

if __name__=="__main__":
	test_stackoperations()