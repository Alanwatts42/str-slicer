import re
import os
import os.path as path

tgt = input("path of logfile:")  # log to be searched
# error = input("enter error to search for:")

def error_search(srchlog):
    
    results = []
    line_num = 0
    
    pattern = re.compile(".*error.*", re.IGNORECASE)
    
    with open(srchlog, 'rt') as logfile:
        for entry in logfile:
            line_num += 1
            if pattern.search(entry) is not None:
                results.append((line_num, entry.rstrip('\n')))

    for result in results:
        print("Line " + str(result[0]) + ": " + result[1])

    


if __name__ == '__main__':
    
    if path.isfile(tgt) is True:
        error_search(tgt)
