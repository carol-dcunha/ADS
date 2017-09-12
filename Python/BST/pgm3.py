import bst

def test_bstoperations():
	obj1=bst.BST()
	obj1.addNode(30)	
	obj1.addNode(40)
	obj1.addNode(10)
	obj1.addNode(20)

	obj2=bst.BST()
	obj2.addNode(50)	
	obj2.addNode(40)

	obj3=bst.BST()
	obj3.addNode(10)	
	obj3.addNode(20)
	obj3.addNode(30)
	obj3.addNode(40)

	assert(obj1.height()==3)
	assert(obj3.height()==4)
	assert(obj2.height()==2)
	
if __name__=="__main__":
	test_bstoperations()