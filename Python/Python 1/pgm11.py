import sys,os,re

def findfiles(path,pattern):
	os.chdir(path)
	regex=re.compile(pattern)
	for item in os.listdir(path):
		os.chdir(path)
		if os.path.isfile(item):
			if re.search(regex,item)!=None:
				print os.path.abspath(item)
		elif os.path.isdir(item):
			findfiles(os.path.abspath(item),pattern)


if __name__ == "__main__":
	if(len(sys.argv)>2):
		path=sys.argv[1]
		pattern=sys.argv[2]
		findfiles(path,pattern)
	else:
		print("Insufficient arguments")
