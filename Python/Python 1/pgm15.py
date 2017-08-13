def groups(lst,size):
	group_lst=[]
	count=0
	lstlen=len(lst)
	if size > lstlen:
		print "Size larger than list size"
	else:
		while count < lstlen:
			if size+count < lstlen:
				group_lst.append(lst[0+count:size+count])
			else:
				group_lst.append(lst[0+count:lstlen])	
			count=count+size
		print "Smaller lists:"
		for item in group_lst:
			print item


if __name__ == "__main__":
	lst=[]
	print "Enter number of items in list: ",
	num=int(raw_input())
	print "Enter the items:"
	for i in range(num):
		lst.append(raw_input())
	print "Enter size to create smaller lists: ",
	size=int(raw_input())
	print "Given list: ",lst
	groups(lst,size)

	

