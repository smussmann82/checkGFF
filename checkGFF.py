#!/usr/bin/env python

from comline import ComLine
from gff import GFF
from binsearch import BIN

import sys

def main():
	input = ComLine(sys.argv[1:])
	gff=GFF(input.args.gff)

	mylist=gff.getList(input.args.acc)
	binsearch = BIN(mylist,input.args.start,input.args.end)
	binsearch.binarySearch()

main()

raise SystemExit
