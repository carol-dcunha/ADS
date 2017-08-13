class ExpandableStack:
	
	
	def __init__(self):
		self.count=0
		self.capacity=2
		self.data=[None]*self.capacity


	def isFull(self):
		return self.capacity==self.count


	def push(self,key):
		if self.isFull():
			self.resize(self.capacity*2)
		self.data[self.count]=key
		self.count+=1


	def isEmpty(self):
		return self.count==0


	def pop(self):
		if not self.isEmpty():
			self.count-=1
			key=self.data[self.count]
			self.data[self.count]=None
			if 0<self.count<=(self.capacity//4):
				self.resize(self.capacity//2)
			return key


	def length(self):
		return self.count


	def peak(self):
		return self.data[self.count-1]


	def resize(self,new_capacity):
		old_length=len(self.data)
		if new_capacity<self.capacity:
			for i in range(new_capacity,old_length):
				self.data.pop()
		else:
			for i in range(old_length,new_capacity):
				self.data.append(None)
		self.capacity=new_capacity


	def firstElement(self):
		return self.data[0];