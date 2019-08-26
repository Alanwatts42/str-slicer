# Str-slicer: Project Outline


""" 
The Primary use case for this tool will be to read text from any source,
especially unorganized sources which are traditionally difficult to go
through and reformat by hand, and then reformat said text into a csv, 
json, or just a more readable text file.
"""

# Parse

The Parse module houses the core functionality used to parse and reformat 
text from the user-selected file. Since the input file could be any
filetype that contains text, a 'slicer' or parsing module is selected,
which determines exactly how the text data is parsed.

Slicers - Parsing modules, each of which would enable a different method 
of parsing the input data, or a different use-case. Determining which 
slicer is appropriate for which input data is a necessary step in parsing 
the data, since the slicer contains the precise steps used to parse the 
data.  Because these slicers are modular, changing how the input data is 
parsed is simply a matter of using a different slicer. This also makes it 
much easier for me to organize these parsing methods.

    1. Input algorithms
        a. Sort
        verify
        b. Pre-processing
        verify
        c. pass data to parser

    2. Parsing        
        a. Receive input data
        verify
        b. Choose a slicer (based on type of data & use-case)
        verify
        c. Parse the data using the chosen slicer
        verify
        d. Pass to output algorithm to be exported

    2. Output algorithm
        a. Receive file from input
        verify
        b. Print - assumes Input alg determines filetype
        verify
        c. Output to file

### Should 'input', 'parse', and 'output' be seperate steps, or should they be combined together?
 - If I start with each process as its own separate script, and realize later that the other combining them would be better, it would perhaps be easier to change my approach if I simply had to combine these processes together than if I had to seperate them.
 - A single process may prove to be useful on it's own, without the others. If that is the case, having them seperated would make it easier to apply any single process to another problem without having to apply all of them at once to that other problem.
 - The project as a whole is more versatile if the processes are seperated, because it enables us to deploy them in a variety of combinations, or even rearrange them to apply them in a different order if necessary.

## Scan
 - Iterate through the document, line by line, and read text into Parse 
to be processed.

## Slice
 - Take apart text from scan function and output it into an ordered dict
dict will then get passed to another function (or module) to be
exported to whatever the output format will be (json, xml, text, csv)

# Export
 - After text has been converted to a more digestable form, such as a 
dictionary after having been processed by Parse.py, this Export module 
will convert the data structure (list or dict) with the text data into
whatever format the user selects: Json, CSV, XML, HTML, Text.


