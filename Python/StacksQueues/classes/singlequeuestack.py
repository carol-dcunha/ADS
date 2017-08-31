import circularqueue as cq

class SingleQueueStack:

	def __init__(self):
		self.queue=cq.CircularQueue()

	def push(self, key):
		queue_data=[]
		while not self.queue.isEmpty():
			queue_data.append(self.queue.dequeue())
		self.queue.enqueue(key)
		for item in queue_data:
			self.queue.enqueue(item)

	def pop(self):
		return self.queue.dequeue()

	def length(self):
		return self.queue.length()

	def peak(self):
		return self.queue.data[0]
