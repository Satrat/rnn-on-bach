from Node import Node

class Midi_Queue:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def get_head(self):
		return self.head

	def get_tail(self):
		return self.tail

	def check_empty(self):
		if(self.head == None and self.tail == None):
			return True

		return False

	def push(self, n):
		if(self.check_empty()):
			self.head = n
			self.tail = n 
		else:
			self.tail.set_next(n)
			self.tail = n

		self.size = self.size + 1

		n.set_next(None)

	def print_size(self):
		print "current queue size: ",self.size

	def pop(self):
		if(self.check_empty()):
			return None

		popped = self.head.get_file()
		if(self.head == self.tail):
			self.tail = None
			self.head = None
		else:
			self.head = self.head.get_next()

		self.size = self.size - 1
		return popped


