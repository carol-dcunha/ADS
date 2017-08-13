import classes.leakystack as ls

def test_leakystack():

	stk=ls.LeakyStack()
	stk.push(10)
	stk.push(20)
	stk.push(30)
	stk.push(40)
	stk.push(50)
	stk.push(60)
	stk.push(70)
	stk.push(80)
	stk.push(90)
	stk.push(100)
	assert(stk.length()==10)
	stk.push(110)
	assert(stk.length()==10)
	assert(stk.peak()==110)
	assert(stk.bottomElement()==20)
	stk.push(120)
	assert(stk.length()==10)
	assert(stk.peak()==120)
	assert(stk.bottomElement()==30)
	

if __name__=="__main__":
	test_leakystack()

