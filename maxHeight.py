def maxHeight(s):
	l=0
	r=len(s)-1
	area=0
	while(l<r):
		area = max( area, min(s[l], s[r]) * (r-l) )
		if s[l] <= s[r]:
			l+=1
		else:
			r-=1
	print(area)

if __name__ == "__main__":
	maxHeight([1,1])