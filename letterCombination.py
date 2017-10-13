def letterCombination(digits):
	if '' == digits: return []
	kvmaps = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'}

	ret=['']
	for c in digits:
		tmp=[]
		for y in ret:
			#print (y)
			for x in kvmaps[c]:
				tmp.append(y+x)
				print(tmp)
		ret=tmp
	print ret

if __name__ == '__main__':
	letterCombination('2')