from __future__ import print_function

import collections

class BIN():
	'Class for conducting a binary search on an array'
	

	def __init__(self, array, start, end):
		#member variables
		self.l = array
		self.s = start
		self.e = end
		self.length = len(self.l)
		print(self.length)

	def binarySearch(self):
		low=1
		high=self.length
		middle=int
		
		found=False
		while( found==False and high >= low ):
			middle = (low + high)/2
			if(self.checkArray(middle)==True):
				print("Found")
			else:
				print("Not Found")
				print(self.l[middle])
				if(self.upordown(middle)==True):
					low=middle+1
				else:
					high=middle-1


	def checkArray(self,i):
		line = self.l[i].split()
		if( (self.e < line[4] and self.e > line[3] ) or ( self.s < line[4] and self.s > line[3] ) ):
			return True
		else:
			return False

	def upordown(self,i):
		line = self.l[i].split()
		if(self.e > line[4] and self.s > line[4]):
			return True
		else:
			return False
