def rollAlpha(s, roll):
	myDict={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,
	'l':11,'m':12, 'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,
	'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
	myArr=['a','b','c','d','e','f','g','h','i','j','k','l','m'
	'n','o','p','q','r','s','t','u','v','w','x','y','z']
	rollCountDict=dict()
	for i in range(1, len(s)+1):
		count = 0
		for rollVal in roll:
			if rollVal >=i:
				count+=1
		rollCountDict[i]=count
	s = list(s)
	print(rollCountDict)
	for key, value in rollCountDict.items():
		myArrIdx = myDict[s[key-1]] + (value%26)
		if myArrIdx == 26:
			myArrIdx =0
		s[key-1] = myArr[ myArrIdx ]
	s = ''.join(s)
	print s
	#print len(myArr)


if __name__ == "__main__":
	rollAlpha('abcdcasdfg', [4,1,5,2, 3, 2 ,3, 4, 8, 10])


	#1, 2, 3, 2 ,3, 4, 8