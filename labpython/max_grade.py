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

    maxgrade = 0
    maxgrade_student_name = "XXXXX XXXX"
    for line in list(fp):
        items = line.split('\t')
        if len(items) < 4:
            continue
        grade = float(items[3][:-1])
        if grade > maxgrade:
            maxgrade = grade
            maxgrade_student_name = items[1] + " " + items[0]
    print maxgrade, maxgrade_student_name


if __name__ == "__main__":
    sys.exit(main())
