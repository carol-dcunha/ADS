class BST:

	class TreeNode:
		def __init__(self,val):
			self.data=val
			self.left=None
			self.right=None

	def __init__(self):
		self.root=None
		self.count=0
		self.leafcount=0

	def isEmpty(self):
		return self.count==0

	def length(self):
		return self.count

	def addNode(self,key):
		parent=current=self.root
		while current is not None and key!=current.data:
			parent=current
			if key<current.data:
				current=current.left
			elif key>current.data:
				current=current.right
		if current is None:
			new_node=self.TreeNode(key)
			if parent is None:
				self.root=new_node
			elif key<parent.data:
				parent.left=new_node
			elif key>parent.data:
				parent.right=new_node
			self.count+=1


	def deleteNode(self,key):
		if not self.isEmpty():
			self.root=self._delete(self.root,key)

	def _delete(self,node,key):
		if node is None:
			return node
		if key<node.data:
			node.left=self._delete(node.left,key)
		elif key>node.data:
			node.right=self._delete(node.right,key)
		elif node.left and node.right:
			temp=self._findMin(node.right)
			node.data=temp.data
			node.right=self._delete(node.right,node.data)
		else:
			if node.left is None:
				node=node.right
			else:
				node=node.left
			self.count-=1
		return node

	def _findMin(self,node):
		if node.left is None:
			return node
		else:
			return self._findMin(node.left)


	def isMember(self,key):
		if not self.isEmpty():
			current=self.root
			flag=False
			while current is not None:
				if key==current.data:
					flag=True
					break
				elif key>current.data:
					current=current.right
				elif key<current.data:
					current=current.left
			return flag

	def getRoot(self):
		if not self.isEmpty():
			return self.root.data


	def minElement(self):
		if not self.isEmpty():
			current=self.root
			while current.left is not None:
				current=current.left
			return current.data

	def maxElement(self):
		if not self.isEmpty():
			current=self.root
			while current.right is not None:
				current=current.right
			return current.data


	def inorder(self):
		if not self.isEmpty():
			node=self.root
			self._inorder(node)

	def _inorder(self,node):
		if node:
			self._inorder(node.left)
			print node.data," ",
			self._inorder(node.right)


	def preorder(self):
		if not self.isEmpty():
			node=self.root
			self._preorder(node)

	def _preorder(self,node):
		if node:
			print node.data," ",
			self._preorder(node.left)
			self._preorder(node.right)


	def postorder(self):
		if not self.isEmpty():
			node=self.root
			self._postorder(node)

	def _postorder(self,node):
		if node:
			self._postorder(node.left)
			self._postorder(node.right)
			print node.data," ",


	def leafCount(self):
		node=self.root
		self._getLeafCount(node)
		return self.leafcount

	def _getLeafCount(self,node):
		if node.left:
			self._getLeafCount(node.left)
		if node.right:
			self._getLeafCount(node.right)
		if not node.left and not node.right:
			self.leafcount+=1


	def compareTrees(self,tree2):
		res=self._compare(self.root,tree2.root)
		return res

	def _compare(self,tree1,tree2):
		if tree1.left and tree2.left:
			res=self._compare(tree1.left,tree2.left)
			if not res:
				return False
		if tree1.right and tree2.right:
			res=self._compare(tree1.right,tree2.right)
			if not res:
				return False
		if tree1.data == tree2.data:
			return True
		else:
			return False


	def height(self):
		res=self._height(self.root)
		return res

	def _height(self,node):
		if not node:
			return 0
		else:
			return 1 + max(self._height(node.left),self._height(node.right))


