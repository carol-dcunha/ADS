import classes.limitedstack as ls

class LeakyStack(ls.LimitedStack):

	def push(self,key):
		if self.isFull():
			datalist=[]
			for i in range((self.length())-1):
				datalist.append(self.pop())
			self.pop()
			for i in range(len(datalist)):
				self.push(datalist.pop())
		self.data[self.count]=key
		self.count+=1
