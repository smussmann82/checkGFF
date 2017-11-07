from __future__ import print_function

import collections

class LIN():
	'Class for conducting a linear search on an array'
	

	def __init__(self, array, start, end):
		#member variables
		self.l = array
		self.s = start
		self.e = end
		self.length = len(self.l)
		print(self.length)

	def linearSearch(self):
		for line in self.l:
			temp = line.split()
			if( (int(self.e) < int(temp[4]) and int(self.e) > int(temp[3]) ) or ( int(self.s) < int(temp[4]) and int(self.s) > int(temp[3]) ) ):
				#print("Found")
				print(line)
			#else:
				#print("Not Found")

