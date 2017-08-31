class CircularQueue:


	def __init__(self):
		self.front=0
		self.size=0
		self.capacity=2
		self.data=[None]*self.capacity


	def length(self):
		return self.size


	def isEmpty(self):
		return self.size==0


	def isFull(self):
		return self.size==self.capacity


	def enqueue(self,key):
		if self.isFull():
			self.capacity*=2
			self.resize(self.capacity)
		next=(self.front+self.size)%self.capacity
		self.data[next]=key
		self.size+=1


	def dequeue(self):
		if not self.isEmpty():
			self.size-=1
			key=self.data[self.front]
			self.data[self.front]=None
			self.front=(self.front+1)%self.capacity
			if 0<self.size<=(self.capacity//4):
				self.capacity=self.capacity//2
				self.resize(self.capacity)
			return key


	def resize(self,new_capacity):
		old_queue=self.data
		walk=self.front
		self.data=[None]*new_capacity
		for i in range(self.size):
			self.data[i]=old_queue[walk]
			walk=(walk+1)%len(old_queue)
		self.front=0


	def rotate(self):
		if not self.isEmpty():
			key=self.data[self.front]
			self.data[self.front]=None
			self.enqueue(key)
			self.size-=1
			self.front=(self.front+1)%self.capacity


	def firstElement(self):
		return self.data[self.front]


	def lastElement(self):
		return self.data[(self.front+self.size-1)%self.capacity]
