# -*- coding: UTF-8 -*-
import os
import os.path

"""For testing techniques for text parsing without building ui"""

def getpath(dir_lo = '.'):
    cp = os.getcwd()
    acp = os.path.abspath(cp)
    output acp.split(os.path.sep)

def grabfile(args):
    infile = open("data/aptlist.txt")

   outfile = open("data/output.csv", 'w')

    for i in range(1):
        infile.next() # skip first line
    for line in infile:
        outfile.writelines(lines, reps)

def writefile():
    pass

if __name__ == '__main__':
    print(getpath())
