import classes.singlylinkedlist as sll

def test_compareList():
	slist1=sll.SinglyLinkedList()
	slist2=sll.SinglyLinkedList()
	slist3=sll.SinglyLinkedList()
	slist4=sll.SinglyLinkedList()

	slist1.addFirst(50)
	slist1.addFirst(20)
	slist1.addLast(30)
	slist1.addFirst(40)

	slist2.addFirst(30)
	slist2.addFirst(50)
	slist2.addFirst(20)
	slist2.addFirst(40)

	slist3.addFirst(40)
	slist3.addFirst(50)
	slist3.addFirst(30)
	slist3.addFirst(40)

	slist4.addFirst(67)
	slist4.addFirst(90)
	slist4.addLast(2)
	slist4.addFirst(40)
	slist4.addLast(5)

	assert(slist1.compareList(slist2)==True)
	assert(slist3.compareList(slist2)==False)
	assert(slist3.compareList(slist4)==False)

if __name__=="__main__":
	test_compareList()