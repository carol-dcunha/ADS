import bst

def test_bstoperations():
	obj=bst.BST()
	obj.addNode(30)	
	obj.addNode(40)
	obj.addNode(10)
	obj.addNode(20)
	assert(obj.getRoot()==30)
	assert(obj.isMember(10)==True)
	assert(obj.isMember(60)==False)
	assert(obj.length()==4)
	assert(obj.minElement()==10)
	assert(obj.maxElement()==40)
	obj.deleteNode(30)
	assert(obj.getRoot()==40)
	obj.deleteNode(40)
	assert(obj.getRoot()==10)
	assert(obj.length()==2)


if __name__=="__main__":
	test_bstoperations()