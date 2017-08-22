import classes.doublylinkedlist as dl

def test_emptyList(slist):
	assert(slist.isEmpty()==True)
	assert(slist.length()==0)	

def test_listInsertion(slist):
	slist.addFirst("Hello")
	assert(slist.isEmpty()==False)
	assert(slist.length()==1)
	slist.addLast("DoublyLinkedList")
	slist.addLast(10)
	slist.addFirst(20)
	assert(slist.length()==4)

def test_listDeletion(slist):
	assert(slist.deleteLast()==10)
	assert(slist.deleteFirst()==20)
	assert(slist.length()==2)
	assert(slist.firstElement()=="Hello")
	assert(slist.lastElement()=="DoublyLinkedList")

def test_listSearch(slist):
	assert(slist.isMember("Hello")==True)
	assert(slist.isMember(20)==False)


def test_listOperations():
	dlist=dl.DoublyLinkedList()
	test_emptyList(dlist)
	test_listInsertion(dlist)
	test_listDeletion(dlist)
	test_listSearch(dlist)


if __name__=="__main__":
	test_listOperations()