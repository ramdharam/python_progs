def longestPalindrome(s):
	"""
	Dynamic Programming

	"""
	strLen = len(s)
	maxLen = 0
	tempTable = [ [None] * strLen ] * strLen

	### 1 char len strings
	for i in xrange(strLen):
		tempTable[i][i] = True

	maxLen = max(maxLen, 1)

	### 2 character length strings
	for i in xrange(strLen-2):
		if s[i]==s[i+1]:
			tempTable[i][i+1]= True
			maxLen = max(maxLen, 2)


	### for 3 character length strings
	for k in xrange(2, strLen):
		for i in xrange(0, strLen-k):
			j = i+k
			if s[i]==s[j] and tempTable[i+1][j-1]==True:
				tempTable[i][j]==True
				maxLen = max(maxLen, j-i+1)

	print(maxLen)
	print(tempTable[1][12])



if __name__ == "__main__":
	longestPalindrome("aaaaabbbbaaaa")	