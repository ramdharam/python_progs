def median(arr):
	"""
	"""
	l = len(arr)
	if l%2==0:
		return (arr[l/2-1] + arr[l/2])/2
	else:
		return (arr[l/2])


def findMedian(l1, l2):

	if len(l1) ==0:
		return -1
	elif len(l1) == 1:
		return (l1[0] + l1[0])/2
	elif len(l1)==2:
		#print(max(l1[0],l2[0]))
		#print(min(l1[1], l2[1]))
		return ( ( max(l1[0],l2[0]) + min(l1[1], l2[1]) ) / 2)


	while len(l1)>2 and len(l2) >2:
		med_l1 = median(l1)
		med_l2 = median(l2)

		if med_l1 < med_l2:
			if len(l1)%2==0:
				return findMedian(l1[len(l1)/2 -1: ], l2[ :len(l2)/2] )
			else:
				return findMedian(l1[len(l1)/2:], l2[:len(l2)/2+1])

		elif med_l1 == med_l2:
			return med_l1
		else:
			if len(l1)%2==0:
				return findMedian(l1[:len(l1)/2], l2[len(l2)/2:] )
			else:
				return findMedian(l1[:len(l1)/2 + 1], l2[len(l2)/2:])

if __name__ == "__main__":
	a=[1,2,3,5,8]
	b=[4,5,6,8,9]

	print(findMedian(a,b))
			
	
