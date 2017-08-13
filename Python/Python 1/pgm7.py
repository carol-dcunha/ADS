import sys
import os

def ls(path):
	for item in os.listdir(path):
		print item


if __name__ == "__main__":
	if(len(sys.argv)>1):
		path=sys.argv[1]
	else:
		path=os.getcwd()
	ls(path)
