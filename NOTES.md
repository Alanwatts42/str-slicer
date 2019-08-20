# str-slicer: related notes

## text parsing

### `open()`
- built-in function for accessing a file 
- if reading a text file, can open `example.txt` and read contents into a string variable.

<br>

example:
```
myfile = open("example.txt", "rt") # open example.txt for reading text
contents = myfile.read()           # read entire file into a string
myfile.close()                     # close the file

print(contents)                    # print contents (derr)
```
in this example:
- `myfile` is the name given to this file object
- the "rt" parameter in the `open()` function means "we're opening this file to read text data"
- if we save this python script as `read.py`, and then `python3 read.py`, 
the output will be the contents of `example.txt`, which will be exclusively 
text, both because of the file type .txt, and the "rt" parameter which 
specifically reads a file as text.

### `with open`
- it is important to close your open files ASAP - open the file, perform the operation, then close it.
- as such, it is good practice to use `with open... as` rather than `open()... close()`.
- `with open...as` is the cleanest way to open a file, operate on it, and close the file ,all in one easy-to-read bock of code.
- the file is automatically closed when the code block completes, as opposed to `open()` which requires you to then manually `close()`

using `with open` we can rewrite the previous example:
```
with open ('example.txt, 'rt') as myfile:  # open example.txt for reading text
    contents = myfile.read()               # read the entire file contents into a string
print(contents)                            # print the string
```

this will produce the same output as the previous example, which will be the entire text contents of the `example.txt` file to the terminal.

## reading text files line by line as `iterators`

`iterator` - a type of python object which behaves in certain ways when operated on repeatedly.
 - for example, you can use a `for loop` to operate on a file object repeatedly, and each time the same operation is performed (i.e. the `read text` operation), you'll receive a different, or "next," result
 - for text files, the file object iterates one line of text at a time
 - the file object considers one line of text a "unit" of data, so we can use a `for...in` loop statement to iterate on the data one line at a time.

example:
```
with open ('example.txt', 'rt') as myfile: # open example.txt for text read
    for myline in myfile:                  # read each line to a string
        print(myline)                      # print that string, repeat
```
 - the output will still be all of the file contents, but each line will be a separate string rather than the entire file being contained in one string called 'contents'
 - this is always preferable to reading entire file text contents into one string for many reasons, but primarily due to ease of parsing and working with the file contents, and the possibility of errors due to memory limits if reading large text file into one string, whereas separating files into individual lines allows us to read a file of any size into strings we can work with in python without concern for memory limitations.
 - the text output from this example is cosmetically different from the previous example in one major way: it has a linebreak after each line, essentially it is double-spaced. This is because one linebreak is from the text file itself for each new line already there, but a second one is added by the `print()` function as it always adds a linebreak automatically at the end of whatever you've asked it to print. 

### storing output from `for` loop of an iterator as a `list` variable

`lists` - similar to, but not the same as, `arrays` in C or Java.
 - a python list contains `indexed` data, of varying lengths and types.
 
example:
```
mylines = []                             # Declare an empty list named mylines.
with open ('lorem.txt', 'rt') as myfile: # Open lorem.txt for reading text data.
    for myline in myfile:                # For each line, stored as myline,
        mylines.append(myline)           # add its contents to mylines.
print(mylines)                           # Print the list.
```
the output of this would be a little different from the previous `print()` example.
 - original example of whole document read into `content` variable:
 ```
 line 1.
 line 2.
 line 3.
 line 4.
 ```
 
 - `for...as` example `print()` output:
 ```
 line 1.

 line 2.

 line 3.

 line 4.
 ```
 
 - printing `mylines` after reading previous output into a `list` object:
 ```
 ['line 1.\n', 'line 2.\n', 'line 3.\n', 'line 4.\n']
 ```
- this is the raw contents of the list, in its raw `object` form, a list is represented as a comma-delimited list, in this case a list of strings, each string being one line of text ending with a `\n`
- here, each element is represented as a string, and each newline is represented as its `escape character` sequence, `\n`.
-

