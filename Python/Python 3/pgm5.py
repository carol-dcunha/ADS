import classes.singlylinkedlist as sll


def test_reverseList():
	slist=sll.SinglyLinkedList()
	slist.addFirst(50)
	slist.addFirst(20)
	slist.addLast(30)
	slist.addFirst(40)
	slist.addLast(10)
	slist.addLast(80)
	slist.addFirst(70)

	assert(slist.length()==7)
	assert(slist.firstElement()==70)
	assert(slist.lastElement()==80)
	slist.reverseList()
	assert(slist.length()==7)	
	assert(slist.lastElement()==70)
	assert(slist.firstElement()==80)
	

if __name__=="__main__":
	test_reverseList()