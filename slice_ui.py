# encoding:utf-8
import argparse
import csv
import os
import easygui as gui


class gui:
    
    def openprompt():
        openfile = gui.fileopenbox(
            msg="Open",
            title="Select file to parse",
            default='*',
            filetypes=None,
            multiple=False
        )
        return openfile
        
    inputfile = open(openfile)
    outputfile = open(savefile, 'w')

    for i in range(1):
        inputfile.next()  # skip lines with no data
    for line in inputfile:
        outputfile.writelines(line, reps)

    for line in inputfile:
        outputfile.writelines(data_parser(line, reps))

    inputfile.close()
    outputfile.close()

    # User saves new parsed .csv file containing data from original file
    savefile = gui.filesavebox(
        msg="Select where to save new parsed data file",
        title="Save Parsed Data",
        default='newdata.csv',
        filetypes="*.csv"
    )

