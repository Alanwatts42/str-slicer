
# -*- coding: UTF-8 -*-

import easygui as gui


def data_parser(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i.j)
    return text


def main():

    # User selects unspecified type of file, probably .txt
    datafile = gui.fileopenbox(msg="Open", title="Select file to parse",
                               default='*', filetypes=None, multiple=False)

    # User saves new parsed .csv file containing data from original file
    savefile = gui.filesavebox(
                               msg="Select where to save new parsed data file",
                               title="Save Parsed Data", default='newdata.csv',
                               filetypes="*.csv")

    reps = {
            '"NAN"': 'NAN',
            '"': '',
            '0-': '0,',
            '1-': '1,',
            '2-': '2,',
            '3-': '3,',
            '4-': '4,',
            '5-': '5,',
            '6-': '6,',
            '7-': '7,',
            '8-': '8,',
            '9-': '9,',
            ' ': ',',
            ':': ','
    }

    inputfile = open(datafile)
    outputfile = open(savefile, 'w')

    for i in range(1):
        inputfile.next()  # skip lines with no data
    for line in inputfile:
        outputfile.writelines(line, reps)

    for line in inputfile:
        outputfile.writelines(data_parser(line, reps))

    inputfile.close()
    outputfile.close()


if __name__ == '__main__':
    main()
