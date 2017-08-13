import classes.doubleendedqueue as dq

def calculateCapital(translist):

	queshare=dq.DoubleEndedQueueArray()
	queamount=dq.DoubleEndedQueueArray()
	sum=0
	for item in translist:

		lst=item.split()
		x=int(lst[1])
		y=int(lst[5])

		if lst[0]=="buy":
			queshare.addLast(x)
			queamount.addLast(y)

		else:
			while x!=0:
				if not queshare.isEmpty():
					share=queshare.deleteFirst()
					amount=queamount.deleteFirst()
					if x>share:
						sum+=share*(y-amount)
						x-=share
					else:
						sum+=x*(y-amount)
						queshare.addFirst(share-x)
						queamount.addFirst(amount)
						x=0
				else:
					return None
	return sum

def test_calculatecapital():

	translist=["buy 100 shares at Rs 20 each","buy 20 shares at Rs 24 each","buy 200 shares at Rs 36 each","sell 150 shares at Rs 30 each"]
	assert(calculateCapital(translist)==940)

	translist=["buy 20 shares at Rs 24 each","buy 200 shares at Rs 36 each","sell 150 shares at Rs 30 each"]
	assert(calculateCapital(translist)==-660)

	translist=["buy 100 shares at Rs 20 each","buy 20 shares at Rs 24 each","sell 150 shares at Rs 30 each"]
	assert(calculateCapital(translist)==None)

if __name__=="__main__":
	test_calculatecapital()
