import sys
import os

def onlyfiles(path):
	for item in os.listdir(path):
		if os.path.isfile(item):
			print item


if __name__ == "__main__":
	if(len(sys.argv)>1):
		path=sys.argv[1]
	else:
		path=os.getcwd()
	os.chdir(path)
	onlyfiles(path)
