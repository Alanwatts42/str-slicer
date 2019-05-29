# -*- coding: UTF-8 -*-
import os
import os.path

"""testing techniques for text parsing without building ui"""

def getpath(dir_lo = '.'):
    cp = os.getcwd()
    acp = os.path.abspath(cp)
    return acp.split(os.path.sep)

def slicegrabber(pth=''):

    with open('pth', 'r') as infile  # open and close file using 'with'
    # 'r' reader arg used for infile

    with open('pth', 'w') as outfile
    # 'w' writer arg used for outfile to write to


    for line in infile.readlines():
        print(line, end='')

        infile.next() # skip first line
    for line in infile:
        outfile.writelines(lines, reps)

def slicewriter():
    pass



# custom file reader class template:

class slicereader():

    def __init__(self, file_path):

        self.__path = file_path

        self.__file_object = none

    def __enter__(self):

        self.__file_object = open(self.__path)

        return self


    def __exit__(self, type, val, tb):

        self..__file_object.close()

        # additional methods

# Now customer class slicereader() can be used similarly
# to Open() built-in method

with slicereader('apt-list.txt') as reader:

    # perform custom class operations

    pass

if __name__ == '__main__':
    print('getpath()')
