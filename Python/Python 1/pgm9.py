import sys
import os

def lastmodfile(path):
	last_time=0
	for item in os.listdir(path):
		time=os.path.getmtime(item)
		if last_time<time:
			last_time=time
			mod_file=item
	print "Latest modified file: ",os.path.abspath(mod_file)
	print "Modification time: ",last_time


if __name__ == "__main__":
	if(len(sys.argv)>1):
		path=sys.argv[1]
	else:
		path=os.getcwd()
	os.chdir(path)
	lastmodfile(path)
