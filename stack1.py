import sys

class Stack:
	def __init__(self, length):
		self.s = [None]*length
		self.top = -1
	def pop(self):
		try:
			self.a=self.s[self.top]
			self.top-=1
			return(self.a)
		except IndexError, ie:
			print("emptry stack")
	def push(self, val):
		try:
			self.s[self.top+1] = val
			self.top +=1
		except IndexError, e:
			print("overflow error")
	def peek(self):
		return(self.s[self.top])
	def isEmpty(self):
		if self.top<0:
			return True
		else:
			return False

def stringRev(string):

	inpLen = len(string)
	st1 = Stack(inpLen)
	out=""
	for i in inp:
		st1.push(i)
	while(st1.isEmpty()==False):
		out = out + st1.pop()
	print(out)

if __name__ == "__main__":
	inp = raw_input("enter String: ")

	#print(type(inp))
	#inp="abcd"
	stringRev(inp)


