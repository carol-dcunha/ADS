import sys

def displayFile():
    if(len(sys.argv)>1):
        filename=sys.argv[1]
        fd=open(filename)
        print(open(filename).read())
    else:
        print("Insufficient arguments")

displayFile()