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

	slist.addAfterElement(100,40)
	assert(slist.length()==8)
	slist.addAfterElement(60,70)
	slist.addAfterElement(90,85)
	assert(slist.length()==9)
	slist.deleteElement(100)
	slist.deleteElement(50)
	slist.deleteElement(85)

if __name__=="__main__":
	test_listInsert()