class DoubleColorStack:
	
	capacity=10
	
	def __init__(self):
		self.redcount=0
		self.bluecount=0
		self.redstart=0
		self.bluestart=DoubleColorStack.capacity//2
		self.data=[None]*DoubleColorStack.capacity


	def blueIsFull(self):
		return DoubleColorStack.capacity==self.bluecount

	def redIsFull(self):
		return self.bluestart==self.redcount

	def blueIsEmpty(self):
		return self.bluecount==0

	def redIsEmpty(self):
		return self.redcount==0



	def redPush(self,key):
		if not self.redIsFull():
			self.data[self.redcount+self.redstart]=key
			self.redcount+=1

	def bluePush(self,key):
		if not self.blueIsFull():
			self.data[self.bluecount+self.bluestart]=key
			self.bluecount+=1

	

	def redPop(self):
		if not self.redIsEmpty():
			self.redcount-=1
			key=self.data[self.redcount+self.redstart]
			self.data[self.redcount+self.redstart]=None
			return key

	def bluePop(self):
		if not self.blueIsEmpty():
			self.bluecount-=1
			key=self.data[self.bluecount+self.bluestart]
			self.data[self.bluecount+self.bluestart]=None
			return key



	def redLength(self):
		return self.redcount

	def blueLength(self):
		return self.bluecount



	def redPeak(self):
		return self.data[self.redstart+self.redcount-1]

	def bluePeak(self):
		return self.data[self.bluestart+self.bluecount-1]

