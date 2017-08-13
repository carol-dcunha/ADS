import classes.doublecolorstack as ds

def test_doublecolorstack():

	stk=ds.DoubleColorStack()
	stk.redPush(10)
	stk.redPush(20)
	stk.bluePush(30)
	stk.bluePush(40)
	stk.bluePush(50)

	assert(stk.blueLength()==3)
	assert(stk.redLength()==2)
	assert(stk.redPeak()==20)
	assert(stk.bluePeak()==50)

	stk.bluePop()
	stk.redPop()

	assert(stk.redPeak()==10)
	assert(stk.bluePeak()==40)

	

if __name__=="__main__":
	test_doublecolorstack()

