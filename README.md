#Str-slicer: Project Outline


""" The Primary use case for this tool will be to read text from any source,
 especially unorganized sources which are traditionally difficult to go
 through and reformat by hand, and then reformat said text into a csv, json,
 or just a better-looking or more readable text file.
"""

#Parse

"""
The Parse module contains functions that will be imported to __main__.py to
provide the functionality needed in order to reformat or parse text from an original rough input file selected by the user, which would then be parsed according to a set of paramaters selected based upon the characteristics of the input file as well as user preference for at least one or two parameters, and then output to a new file (format of output file would be user-selected as well). As this is a work in progress, the focus will be on one function at a time, which will be specialized to be able to parse a certain type of text file effectively. A second function, which would be specialized to parse a second type of text file, or otherwise expand this functionality in a way that is distinct from the first function, will not be started or worked on in any way until the first function has been completed. More important than the software itself is the process. This project is far more valuable as a trial for working out a design process than it likely ever will be for parsing data. Hopefully a tight focus on one singular piece of this software at any one time, and a commitment to finishing one thing before moving on to the next, will prove to be an effective template, or at the very least a good place to start.
"""

##Parse.scan
/#Iterate through the document, line by line, and read text into Parse to be
processed.


##Parse.slice
/#Take apart text from scan function and output it into an ordered dict
/#dict will then get passed to another function (or module) to be
/#exported to whatever the output format will be (json, xml, text, csv)


#Export
"""
After text has been converted to a dataform such as a dictionary after
having been processed by Parse.py, this Export module will contain
functions to handle converting the dictionary with the text data into
whatever format the user selects: Json, CSV, XML, HTML, Text.
"""

##Export.xjson
/#Self-explanatory, may need to import 3rd party json lib


##Export.xcsv
/#Convert and export data to csv

##Export.xxml
/#''

##Export.xhtml
/#''
##Export.xtext
/#'
