# Str-slicer: Project Outline


""" The Primary use case for this tool will be to read text from any source,
especially unorganized sources which are traditionally difficult to go
 through and reformat by hand, and then reformat said text into a csv, json,
 or just a more readable text file.
"""

# Parse

"""
The Parse module houses the functions that can be  imported
to the modules the user interacts with, and provide the core
functionality used to parse and reformat text from 
the user-selected file. Since the input file could be any
filetype that contains text, the module uses a simple 
algorithm to decide exactly how to parse the text data.

    1. Input algorithm
        a. Sort
        verify
        b. Parse
        verify
        c. pass data to output as Python object (dict or list)

    2. Output algorithm
        a. Receive file from input
        verify
        b. Print - assumes Input alg determines filetype
        verify
        c. Output to file


More important than the software itself is the process. '
This project is far more valuable as a trial for working 
out a design process than it likely ever will be for 
parsing data. 

Hopefully a tight focus on one singular 
piece of this software at any one time, and a commitment 
to finishing one thing before moving on to the next, 
will prove to be an effective template, or at the very 
least a good place to start.
"""

## Parse.scan
/#Iterate through the document, line by line, and read text into Parse to be
processed.


## Parse.slice
/#Take apart text from scan function and output it into an ordered dict
/#dict will then get passed to another function (or module) to be
/#exported to whatever the output format will be (json, xml, text, csv)


# Export
"""
After text has been converted to a dataform such as a dictionary after
having been processed by Parse.py, this Export module will convert the 
data structure (list or dict) with the text data into
whatever format the user selects: Json, CSV, XML, HTML, Text.
"""

It's worth mentioning that this readme has a lot more to do with organizing my
own process building this simple python project. As a result, there might be
things described in this readme that I haven't done yet, and may not end up
doing. Since the project itself may change drastically, the same changes may or
may not be reflected here, though I will do my best to keep it updated so it
corresponds with what I actually end up with.

If you're reading this, thanks for checking out my little project, and feel free
to do whatever it is that github and the open source license let you do.
Feedback of any kind is always appreciated, my goal with this is to get better.
Hopefully as this project progresses, it will also serve as something that
potential employers an look at to evaluate my coding. If you are such an
employer, and my coding is passible, go ahead and hire me. You'll be glad you did.

Thank you for reading this document, that is it's purpose after all. Whatever
your reason is for checking out my project, thank you for your attention.
