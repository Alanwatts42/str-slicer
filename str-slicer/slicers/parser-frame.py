#/usr/bin/python3


# function for parsing the data
def data_parser(text, dic):
for i, j in dic.iteritems():
text = text.replace(i,j)
    return text

inputfile = open('test.dat') 
outputfile = open('test.csv', 'w')


# sample text string, just for demonstration to let you know how the data looks
# my_text = '"2012-06-23 03:09:13.23",4323584,-1.911224,-0.4657288,-0.1166382,-0.24823,0.256485,"NAN",-0.3489428,-0.130449,-0.2440527,-0.2942413,0.04944348,0.4337797,-1.105218,-1.201882,-0.5962594,-0.586636'

# dictionary definition 0-, 1- etc. are there to parse the date block delimited with dashes, and make sure the negative numbers are not effected
reps = {
'"NAN"':'NAN',
    '"':'', '0-':'0,','1-':'1,','2-':'2,','3-':'3,','4-':'4,','5-':'5,','6-':'6,','7-':'7,','8-':'8,','9-':'9,', ' ':',', ':':','
}

for i in range(4): inputfile.next() # skip first four lines
for line in inputfile:
    outputfile.writelines(data_parser(line, reps))

inputfile.close()
outputfile.close()
