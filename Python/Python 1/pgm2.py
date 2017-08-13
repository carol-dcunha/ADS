import sys

def wordcount(filename):
	f=open(filename)
	print "Word count:",len(f.read().split())

def linecount(filename):
	print "Line count:",len(open(filename).readlines())

def charcount(filename):
	print "Character count:",len(open(filename).read())

if __name__ == "__main__":
	if(len(sys.argv)>1):
		filename=sys.argv[1]
		wordcount(filename)
		linecount(filename)
		charcount(filename)
	else:
		print("File name not provided")
