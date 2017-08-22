import singlylinkedlist as sll

class UniqueSinglyLinkedList(sll.SinglyLinkedList):

	def addFirst(self,val):
		if not self.isMember(val):
			new_node=self._Node(val)
			if not self.isEmpty():
				new_node.next=self.head
				self.head=new_node
			else:
				self.head=self.tail=new_node
			self.count+=1

	def addLast(self,val):
		if not self.isMember(val):
			new_node=self._Node(val)
			if not self.isEmpty():
				self.tail.next=new_node
				self.tail=new_node
			else:
				self.head=self.tail=new_node
			self.count+=1