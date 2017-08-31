class LimitedStack:
	
	stack_capacity=10
	
	def __init__(self):
		self.count=0
		self.data=[None]*LimitedStack.stack_capacity

	def isFull(self):
		return LimitedStack.stack_capacity==self.count

	def push(self,key):
		if not self.isFull():
			self.data[self.count]=key
			self.count+=1

	def isEmpty(self):
		return self.count==0

	def pop(self):
		if not self.isEmpty():
			self.count-=1
			key=self.data[self.count]
			self.data[self.count]=None
			return key

	def length(self):
		return self.count

	def peak(self):
		return self.data[self.count-1]

	def bottomElement(self):
		return self.data[0]
