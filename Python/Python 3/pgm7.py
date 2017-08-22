import classes.singlylinkedlist as sll

def test_unionList():
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

	union_lst=slist1.unionList(slist2)


if __name__=="__main__":
	test_unionList()