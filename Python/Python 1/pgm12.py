import sys,os,re

def findfiles(path,size):
	os.chdir(path)
	for item in os.listdir(path):
		os.chdir(path)
		if os.path.isfile(item):
			if os.path.getsize(item)>size:
				print os.path.abspath(item)
		elif os.path.isdir(item):
			findfiles(os.path.abspath(item),size)


if __name__ == "__main__":
	if(len(sys.argv)>2):
		path=sys.argv[1]
		size=float(sys.argv[2])
		if len(sys.argv)>3:
			sizetype=sys.argv[3]
			if sizetype=='K':
				size*=1024
			elif sizetype=='M':
				size*=1024*1024
			elif sizetype=='G':
				size*=1024*1024*1024
		findfiles(path,size)
	else:
		print("Insufficient arguments")
