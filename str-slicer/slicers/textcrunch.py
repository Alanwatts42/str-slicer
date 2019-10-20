#!/usr/bin/python3.6
"""
Remove empty spaces, new lines, etc. in a document, and condense 
it down to easily parsible components
"""
from os.path import abspath

raw_doc = input("enter full path of document: ")
aw_doc = abspath(str(raw_doc))
with open(raw_doc, 'r') as rd:
    all_lines = rd.readlines()
    for line in all_lines:
        # nline = line.replace('\n', ' ').replace('\r', '')
        with open('baked.txt', 'w') as b:
            b.write(line.replace('\n', ' ').replace('\r', ''))
