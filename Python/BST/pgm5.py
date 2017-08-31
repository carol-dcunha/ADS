import bst

def test_bstoperations():
	obj=bst.BST()
	obj.addNode(30)	
	obj.addNode(40)
	obj.addNode(10)
	obj.addNode(20)
	assert(obj.minElement()==10)
	assert(obj.maxElement()==40)


if __name__=="__main__":
	test_bstoperations()