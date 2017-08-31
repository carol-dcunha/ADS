import expandablestack as es

class DoubleEndedQueue:

	def __init__(self):
		self.stkQ=es.ExpandableStack()
		self.stkT=es.ExpandableStack()

	def length(self):
		return self.stkQ.length()

	def addLast(self,key):
		self.stkQ.push(key)

	def addFirst(self,key):
		for i in range(self.stkQ.length()):
			self.stkT.push(self.stkQ.pop())
		self.stkQ.push(key)
		for i in range(self.stkT.length()):
			self.stkQ.push(self.stkT.pop())

	def deleteLast(self):
		return self.stkQ.pop()

	def deleteFirst(self):
		for i in range(self.stkQ.length()-1):
			self.stkT.push(self.stkQ.pop())
		key=self.stkQ.pop()
		for i in range(self.stkT.length()):
			self.stkQ.push(self.stkT.pop())
		return key

	def firstElement(self):
		return self.stkQ.firstElement()

	def lastElement(self):
		return self.stkQ.peak()


class DoubleEndedQueueArray:

	capacity=5
	def __init__(self):
		self.data=[]

	def isEmpty(self):
		return len(self.data)==0

	def isFull(self):
		return len(self.data)==DoubleEndedQueueArray.capacity

	def length(self):
		return len(self.data)

	def addLast(self,key):
		if self.isFull():
			self.deleteFirst()
		self.data.append(key)

	def addFirst(self,key):
		if self.isFull():
			self.deleteLast()
		old_data=self.data
		self.data=[]
		self.data.append(key)
		for item in old_data:
			self.data.append(item)

	def deleteLast(self):
		if not self.isEmpty():
			return self.data.pop()

	def deleteFirst(self):
		if not self.isEmpty():
			old_data=self.data[1:]
			key=self.data[0]
			self.data=[]
			for item in old_data:
				self.data.append(item)
			return key

	def firstElement(self):
		return self.data[0]

	def lastElement(self):
		return self.data[-1]
