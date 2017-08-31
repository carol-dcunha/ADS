import classes.singlylinkedlist as sll


def test_minmax():
	slist=sll.SinglyLinkedList()
	slist.addFirst(50)
	slist.addFirst(20)
	slist.addLast(30)
	slist.addFirst(40)
	slist.addLast(10)
	slist.addLast(80)
	slist.addFirst(70)

	assert(slist.getMax()==80)
	assert(slist.getMin()==10)

if __name__=="__main__":
	test_minmax()