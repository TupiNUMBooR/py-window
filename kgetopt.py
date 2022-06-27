#!/usr/bin/env python3
import getopt
import sys

optlist, args = getopt.getopt(sys.argv[1:], 'abc:d:')
print(optlist)
print(args)
