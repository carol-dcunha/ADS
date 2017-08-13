import sys

def head(filename):
	f=open(filename)
	count=5
	while(count>0):
		str=f.readline()
		if str=='':
			break
		print str,
		count=count-1


if __name__ == "__main__":
	if(len(sys.argv)>1):
		filename=sys.argv[1]
		head(filename)
	else:
		print("File name not provided")
