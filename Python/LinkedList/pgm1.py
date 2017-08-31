import classes.singlylinkedlist as sll

def test_emptyList(slist):
	assert(slist.isEmpty()==True)
	assert(slist.length()==0)	

def test_listInsertion(slist):
	slist.addFirst("Hello")
	assert(slist.isEmpty()==False)
	assert(slist.length()==1)
	slist.addLast("SinglyLinkedList")
	slist.addLast(10)
	slist.addFirst(20)
	assert(slist.length()==4)

def test_listDeletion(slist):
	assert(slist.deleteLast()==10)
	assert(slist.deleteFirst()==20)
	assert(slist.length()==2)
	assert(slist.firstElement()=="Hello")
	assert(slist.lastElement()=="SinglyLinkedList")

def test_listSearch(slist):
	assert(slist.isMember("Hello")==True)
	assert(slist.isMember(20)==False)


def test_listOperations():
	slist=sll.SinglyLinkedList()
	test_emptyList(slist)
	test_listInsertion(slist)
	test_listDeletion(slist)
	test_listSearch(slist)


if __name__=="__main__":
	test_listOperations()