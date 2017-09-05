import bst

def printInorder(obj):
	print "\nInorder Traveral:\t",
	obj.inorder()

def printPostorder(obj):
	print "\nPostorder Traversal:\t",
	obj.postorder()

def printPreorder(obj):
	print "\nPreorder Traversal:\t",
	obj.preorder()

def fillTree(obj):
	obj.addNode(40)
	obj.addNode(25)
	obj.addNode(78)
	obj.addNode(10)
	obj.addNode(32)
	obj.addNode(17)
	obj.addNode(30)
	obj.addNode(93)
	obj.addNode(50)
	obj.addNode(38)
	obj.addNode(3)


if __name__=="__main__":
	obj=bst.BST()
	fillTree(obj)
	printInorder(obj)
	printPreorder(obj)
	printPostorder(obj)
	obj.leafNodes()