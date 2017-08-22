import classes.uniquesinglylinkedlist as usll

def test_uniqueList():
	slist=usll.UniqueSinglyLinkedList()

	slist.addFirst(55)
	slist.addFirst(20)
	slist.addLast(30)
	slist.addFirst(40)
	slist.addFirst(82)
	slist.addFirst(90)
	slist.addLast(29)
	slist.addFirst(40)
	slist.addLast(55)

	assert(slist.length()==7)


if __name__=="__main__":
	test_uniqueList()