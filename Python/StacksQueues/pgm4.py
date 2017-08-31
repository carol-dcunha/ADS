import classes.limitedstack as sc

def transfer(stkS,stkT):
	for i in range(stkS.length()):
		stkT.push(stkS.pop())

def reverseStack(stk):
	stk_temp1=sc.LimitedStack()
	stk_temp2=sc.LimitedStack()
	transfer(stk,stk_temp1)
	transfer(stk_temp1,stk_temp2)	#now stk and stk_temp2 are similar
	transfer(stk_temp2,stk)			#reversed stk

def test_reverseStack():
	stk=sc.LimitedStack()
	stk.push(10)
	stk.push("Hello World")
	stk.push("Welcome")
	reverseStack(stk)
	assert(stk.peak()==10)
	assert(stk.length()==3)
	stk.pop()
	assert(stk.pop()=="Hello World")
	assert(stk.pop()=="Welcome")
	assert(stk.length()==0)

if __name__=="__main__":
	test_reverseStack()