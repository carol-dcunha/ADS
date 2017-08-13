import sys

def sumAll(filename):
	f=open(filename)
	sum=0
	while True:
		str=f.readline()
		if(str==''):
			break
		num=int(str)
		sum=sum+num
	print "Sum: ",sum


if __name__ == "__main__":
	if(len(sys.argv)>1):
		filename=sys.argv[1]
		sumAll(filename)
	else:
		print("File name not provided")
