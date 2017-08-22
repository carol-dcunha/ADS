import classes.singlylinkedlist as sll


def test_listInsert():
	slist=sll.SinglyLinkedList()
	slist.addFirst(50)
	slist.addFirst(20)
	slist.addLast(30)
	slist.addFirst(40)
	slist.addLast(10)
	slist.addLast(80)
	slist.addFirst(70)

	slist.deleteElement(10)
	slist.deleteElement(70)
	assert(slist.length()==5)
	slist.deleteElement(85)
	assert(slist.length()==5)
	

if __name__=="__main__":
	test_listInsert()