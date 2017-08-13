import classes.arraystack as astk

def test_arraystackoperations():
	try:
		stk=astk.ArrayStack()
		stk.push(10)
		stk.push(20)
		stk.push(30)
		stk.push(40)
		stk.push(50)
		stk.push(60)
	except astk.ArrayFullException:
		print "Array Full exception"

if __name__=="__main__":
	test_arraystackoperations()

