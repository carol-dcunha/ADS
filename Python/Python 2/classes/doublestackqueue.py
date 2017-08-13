import expandablestack as es

class DoubleStackQueue:


	def __init__(self):
		self.stkQ=es.ExpandableStack()
		self.stkT=es.ExpandableStack()


	def length(self):
		return self.stkQ.length()


	def enqueue(self,key):
		self.stkQ.push(key)


	def dequeue(self):
		for i in range(self.length()-1):
			self.stkT.push(self.stkQ.pop())
		key=self.stkQ.pop()
		for i in range(self.stkT.length()):
			self.enqueue(self.stkT.pop())
		return key


