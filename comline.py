from __future__ import print_function

import argparse
import os.path

class ComLine():
	'Class for implementing command line options'
	

	def __init__(self, args):
		parser = argparse.ArgumentParser()
		parser._action_groups.pop()
		required = parser.add_argument_group('required arguments')
		optional = parser.add_argument_group('optional arguments')
		required.add_argument("-g", "--gff",
							dest='gff',
							required=True,
							help="Specify a gff file for input."
		)
		required.add_argument("-a", "--acc",
							dest='acc',
							required=True,
							help="Specify genbank accession number."
		)
		required.add_argument("-s", "--start",
							dest='start',
							required=True,
							help="Specify starting coordinate of search sequence."
		)
		required.add_argument("-e", "--end",
							dest='end',
							required=True,
							help="Specify ending coordinate of search sequence."
		)
		
		self.args = parser.parse_args()

		#check if files exist
		self.exists( self.args.gff )

	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print(filename, "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit
