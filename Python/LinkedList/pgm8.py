import classes.singlylinkedlist as sll

def test_intersectionList():
	slist1=sll.SinglyLinkedList()
	slist2=sll.SinglyLinkedList()

	slist1.addFirst(55)
	slist1.addFirst(20)
	slist1.addLast(30)
	slist1.addFirst(40)

	slist2.addFirst(82)
	slist2.addFirst(90)
	slist2.addLast(29)
	slist2.addFirst(40)
	slist2.addLast(55)

	inter_lst=slist1.intersectionList(slist2)
	assert(inter_lst.isMember(40)==True)
	assert(inter_lst.length()==2)
	assert(inter_lst.isMember(82)==False)


if __name__=="__main__":
	test_intersectionList()
