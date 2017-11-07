from __future__ import print_function

import collections

class GFF():
	'Class for working with GFF file'
	

	def __init__(self, f):
		#member variables
		self.gff_file = f
		self.content = list()
		self.features = collections.defaultdict(list)
		
		#functions
		self.readFile()
		#self.printf()
		self.parseFile()

	def readFile(self):
		with open(self.gff_file) as f:
			self.content = [line for line in f.readlines() if not line.startswith('#')]
		self.content = [x.strip() for x in self.content]

	def printf(self):
		for x in self.content:
			print(x)

	def parseFile(self):
		for line in self.content:
			temp = line.split()
			accn = temp[0].split('.')
			self.features[accn[0]].append(line)
		#print(self.features)

	def getList(self,accn):
		return self.features[accn]
