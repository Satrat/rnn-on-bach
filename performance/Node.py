class Node:
	def __init__(self,f):
		self.midi_file = f
		self.next_node = None

	def get_file(self):
		return self.midi_file

	def get_next(self):
		return self.next_node

	def set_next(self,n):
		self.next_node = n