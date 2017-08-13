import sys

def copyfile(file1,file2):
	fd1=open(file1)
	fd2=open(file2,"w+")
	while True:
		str=fd1.readline()
		if(str==''):
			break
		fd2.write(str)


if __name__ == "__main__":
	if(len(sys.argv)>2):
		file1=sys.argv[1]
		file2=sys.argv[2]
		copyfile(file1,file2)
	else:
		print("File name not provided")
