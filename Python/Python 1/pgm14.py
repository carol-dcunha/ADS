def dups(lst):
	new_lst=[]
	for item in lst:
		if item in new_lst:
			print item," ",
		else:
			new_lst.append(item)


if __name__ == "__main__":
	lst=[]
	print "Enter number of items in list: ",
	num=int(raw_input())
	print "Enter the items:"
	for i in range(num):
		lst.append(raw_input())
	print "Given list: ",lst
	print "Duplicates: ",
	dups(lst)

