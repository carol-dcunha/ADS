class MaxHeap:

	def __init__(self,lst=[]):
		self.data=lst
		self._buildheap()

	def length(self):
		return len(self.data)

	def isEmpty(self):
		return self.length()==0

	def getMaximum(self):
		if not self.isEmpty():
			return self.data[0]

	def _parent(self,i):
		return (i-1)//2

	def _leftchild(self,i):
		return (2*i+1)

	def _rightchild(self,i):
		return (2*i+2)

	def _swap(self,i,j):
		self.data[i],self.data[j]=self.data[j],self.data[i]


	def _upheap(self,j):
		parent=self._parent(j)
		if j>0 and self.data[j]>self.data[parent]:
			self._swap(j,parent)
			self._upheap(parent)


	def _downheap(self,j,size):
		if self._leftchild(j)<size:
			left=self._leftchild(j)
			big_child=left
			if self._rightchild(j)<size:
				right=self._rightchild(j)
				if self.data[right]>self.data[left]:
					big_child=right
			if self.data[big_child]>self.data[j]:
				self._swap(big_child,j)
				self._downheap(big_child,size)
	

	def _buildheap(self):
		if not self.isEmpty():
			len=self.length()
			start=(len-2)//2
			for i in range(start,-1,-1):
				self._downheap(i,len)


	def testHeapOrder(self):
		if not self.isEmpty():
			for i in range(self.length()-1,0,-1):
				assert(self.data[i]<=self.data[self._parent(i)])


	def addElement(self,ele):
		self.data.append(ele)
		self._upheap(self.length()-1)

	
	def removeMaximum(self):
		if not self.isEmpty():
			self._swap(0,self.length()-1)
			ele=self.data.pop()
			self._downheap(0,self.length())
			return ele


	def heapSort(self):
		if not self.isEmpty():
			for i in range(self.length()-1,0,-1):
				self._swap(0,i)
				self._downheap(0,i)


	def testSort(self):
		if not self.isEmpty():
			for i in range(0,self.length()-1):
				assert(self.data[i]<=self.data[i+1])

	


	