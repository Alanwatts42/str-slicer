#Str-slicer: Project Outline


""" The Primary use case for this tool will be to read text from any source,
 especially unorganized sources which are traditionally difficult to go
 through and reformat by hand, and then reformat said text into a csv, json,
 or just a better-looking or more readable text file.
"""

#Parse.py

"""
The Parse module contains functions that will be imported to __main__.py to
provide the functionality needed in order to reformat or parse text which can
be written to a new file. Whether the export or 'write' functionality will
live in Parse or in another module is uncertain, but the 'read' and 'process'
phases where the text is receieved and processed or parsed will definitely 
be handled in this module.
"""

##Parse.scan
/#Iterate through the document, line by line, and read text into Parse to be
processed.


##Parse.slice 
/#Take apart text from scan function and output it into an ordered dict
/#dict will then get passed to another function (or module) to be
/#exported to whatever the output format will be (json, xml, text, csv)


#Export.py
"""
After text has been converted to a dataform such as a dictionary after
having been processed by Parse.py, this Export module will contain
functions to handle converting the dictionary with the text data into 
whatever format the user selects: Json, CSV, XML, HTML, Text.
"""

##Export.json
/#Self-explanatory, may need to import 3rd party json lib


##Export.csv
/#Convert and export data to csv

##Export.xml
/#''

##Export.html
/#''
##Export.text
/#'
