import classes.limitedstack as sc

def checkHtmlTags(raw_code):
	stk=sc.LimitedStack()
	j=raw_code.find('<')
	while j!=-1:
		k=raw_code.find('>',j+1)
		tag=raw_code[j+1:k]
		if not tag.startswith('/'):
			stk.push(tag.split()[0])
		else:
			if stk.isEmpty():
				return False
			if tag[1:]!=stk.pop():
				return False
		j=raw_code.find('<',k+1)
	return stk.isEmpty()

def test_checkHtmlTags():
	raw_code1="<HTML><SCRIPT type=\"text/javascript\"></SCRIPT><BODY></BODY></HTML>"
	raw_code2="<HTML><SCRIPT></SCRIPT><BODY border=\"1\" bgcolor=\"red\"><BODY></HTML>"
	raw_code3="<HTML><SCRIPT></SCRIPT><SCRIPT></SCRIPT<BODY></BODY></HTML>"
	assert(checkHtmlTags(raw_code1)==True)
	assert(checkHtmlTags(raw_code2)==False)
	assert(checkHtmlTags(raw_code3)==False)


if __name__=="__main__":
	test_checkHtmlTags()