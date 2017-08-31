import classes.limitedstack as sc

def transfer(stkS,stkT):
	for i in range(stkS.length()):
		stkT.push(stkS.pop())


def mergeStack(stkR,stkS,stkT):
	stk_temp1=sc.LimitedStack()
	stk_temp2=sc.LimitedStack()
	transfer(stkS,stk_temp1)
	transfer(stkT,stk_temp2)
	while stkS.pop():
		None
	for i in range(stk_temp2.length()):
		stkS.push(stk_temp2.pop())
	for i in range(stk_temp1.length()):
		stkS.push(stk_temp1.pop())


def test_mergeStack():
	stkR=sc.LimitedStack()
	stkR.push(1)
	stkR.push(2)
	stkR.push(3)
	
	stkS=sc.LimitedStack()
	stkS.push(4)
	stkS.push(5)
	
	stkT=sc.LimitedStack()
	stkT.push(6)
	stkT.push(7)
	stkT.push(8)
	stkT.push(9)

	mergeStack(stkR,stkS,stkT)
	assert(stkS.peak()==5)
	assert(stkS.length()==6)
	stkS.pop()
	stkS.pop()
	assert(stkS.peak()==9)


if __name__=="__main__":
	test_mergeStack()