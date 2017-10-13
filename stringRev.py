def stringReversal(s):
	"""
	Reverse a string
	"""
	strLen = len(s)
	rev=[None] * len(s)
	for i in xrange(len(s)/2+1):
		rev[strLen-1-i] = s[i]
		rev[i]= s[strLen-1-i]

	rev=''.join(rev)
	print(rev)


if __name__=="__main__":
	stringReversal("code")
