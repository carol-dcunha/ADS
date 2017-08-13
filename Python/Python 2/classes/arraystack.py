import limitedstack as ls


class ArrayFullException(Exception):
    pass


class ArrayStack(ls.LimitedStack):

	maxlen=5
	def __init__(self):
		ls.LimitedStack.stack_capacity=ArrayStack.maxlen
		self.count=0
		self.data=[None]*ArrayStack.maxlen

	def push(self,key):
		if self.isFull():
			raise(ArrayFullException())
		else:
			self.data[self.count]=key
			self.count+=1


