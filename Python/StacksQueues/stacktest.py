import classes.expandablestack as sc

def test_emptystack():
	stk=sc.ExpandableStack()
	assert(stk.isEmpty())
	assert(stk.length()==0)

def test_stackoperations():
	stk=sc.ExpandableStack()
	stk.push(10)
	stk.push("Hello World")
	stk.push("Welcome")
	print stk.data
	assert(stk.peak()=="Welcome")
	assert(stk.length()==3)
	
	assert(stk.pop()!="Hello World")
	assert(stk.length()==2)
	print stk.data
	assert(stk.pop()=="Hello World")
	assert(stk.peak()==10)
	print stk.data
	assert(stk.pop()==10)
	assert(stk.length()==0)

if __name__=="__main__":
	test_emptystack()
	test_stackoperations()