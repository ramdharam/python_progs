import StackClass as sc

def balancedParenthesis(string):
	inp = string
	inpLen = len(inp)

	st1 = sc.Stack(inpLen)
	count=0
	maxCount =0
	for i in inp:
		if i=='(':
			st1.push(i)
			count = count+1
			maxCount = max(maxCount, count)
		elif i==')':
			st1.pop()
			count=count-1
			maxCount = max(maxCount, count)
		else:
			continue

	if st1.isEmpty()==True:
		print (maxCount)
	else:
		print -1



if __name__ == "__main__":
	inp = raw_input("enter string: ")

	balancedParenthesis(inp)


#( ((X)) (((Y))) )