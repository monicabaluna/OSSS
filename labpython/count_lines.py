#!/usr/bin/env python

import sys


def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
    print "Program arguments are:", sys.argv
    print "Number of arguments is:", len(sys.argv)
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    try:
        fp = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid filename."
        usage()
        sys.exit(1)
    print "Number of lines in file is:", len(list(fp))
    fp.seek(0)
    for idx, line in enumerate(list(fp)):
        print "%d: %s" % (idx+1, line),

if __name__ == "__main__":
    sys.exit(main())
