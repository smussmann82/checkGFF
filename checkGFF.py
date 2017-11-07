#!/usr/bin/env python

from comline import ComLine
from gff import GFF

import sys

def main():
	input = ComLine(sys.argv[1:])
	gff=GFF(input.args.gff)

main()

raise SystemExit
