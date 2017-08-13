import classes.limitedstack as sc

def reverseList(lst):
	stk=sc.LimitedStack()
	for i in range(len(lst)):
		stk.push(lst[i])
	for i in range(stk.length()):
		lst[i]=stk.pop()

def test_reverseList():
	lst=[10,"Hello","World","Python"]
	reverseList(lst)
	assert(len(lst)==4)
	assert(lst[0]=="Python")
	assert(lst[-1]==10)

if __name__=="__main__":
	test_reverseList()