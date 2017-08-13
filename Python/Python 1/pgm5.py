import sys

def grep(filename,pattern):
	f=open(filename)
	while True:
		str=f.readline()
		if(str==''):
			break
		if pattern in str:
			print -n str


if __name__ == "__main__":
	if(len(sys.argv)>2):
		filename=sys.argv[1]
		pattern=sys.argv[2]
		grep(filename,pattern)
	else:
		print("File name not provided")
