def fibonocci(num):
	if num==1:
		return 1
	elif num==0:
		return 0
	else:
		return ( fibonocci(num-1) + fibonocci(num-2) )

if __name__ == "__main__":
	print(fibonocci(6))

	#1 1 2 3 5 8
