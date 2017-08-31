class BST:

	class TreeNode:
		def __init__(self,val):
			self.data=val
			self.left=None
			self.right=None

	def __init__(self):
		self.root=None
		self.count=0

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