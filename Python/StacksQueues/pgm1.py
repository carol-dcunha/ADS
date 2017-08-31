import classes.limitedstack as sc

def transfer(stkS,stkT):
	for i in range(stkS.length()):
		stkT.push(stkS.pop())

def test_stackTransfer():
	stkS=sc.LimitedStack()
	stkS.push(10)
	stkS.push("Hello World")
	stkS.push("Welcome")
	stkT=sc.LimitedStack()
	transfer(stkS,stkT)
	assert(stkT.peak()==10)
	assert(stkT.length()==3)
	stkT.pop()
	assert(stkT.pop()=="Hello World")
	assert(stkT.pop()=="Welcome")
	assert(stkT.length()==0)

if __name__=="__main__":
	test_stackTransfer()