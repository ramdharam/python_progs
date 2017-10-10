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