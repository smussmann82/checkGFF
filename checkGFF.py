#!/usr/bin/env python

from comline import ComLine
from gff import GFF
#from binsearch import BIN
from linsearch import LIN

import sys

def main():
	input = ComLine(sys.argv[1:])
	gff=GFF(input.args.gff)

	mylist=gff.getList(input.args.acc)
	#binsearch = BIN(mylist,input.args.start,input.args.end)
	#binsearch.binarySearch()
	linsearch = LIN(mylist,input.args.start,input.args.end)
	linsearch.linearSearch()

main()

raise SystemExit
