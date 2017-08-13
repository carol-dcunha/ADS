import sys
import os

def largestfile(path):
	max_size=0
	for item in os.listdir(path):
		size=os.path.getsize(item)
		if max_size<size:
			max_size=size
			max_file=item
	print "Largest file: ",os.path.abspath(max_file)
	print "Size: ",max_size,"bytes"


if __name__ == "__main__":
	if(len(sys.argv)>1):
		path=sys.argv[1]
	else:
		path=os.getcwd()
	os.chdir(path)
	largestfile(path)
