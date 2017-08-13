def unique(lst):
	unique_lst=[]
	for i in lst:
		if i not in unique_lst:
			unique_lst.append(i)
	return unique_lst


if __name__ == "__main__":
	lst=[]
	print "Enter number of items in list: ",
	num=int(raw_input())
	print "Enter the items:"
	for i in range(num):
		lst.append(raw_input())
	unique_lst=unique(lst)
	print "Given list: ",lst
	print "Unique list: ",unique_lst

