import easygui as gui
import csv
import json

inputfile = gui.fileopenbox()

def write2json():
    with open('output.json', 'w') as f:
        f.write(json.dumps(res, indent=4))
    return 


def read():
    with open ('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]

def batch(content, n=1):
    length = len(content)
    for num_idx in range(0, length, n)):
        yield content[num_idx:min(num_idx+n, length)]

def emit(batched):
    for n, name in enumerate([
        'name', 'description', 'info', 'author', 'year'
    ]):
        yield name, batched[n]

content = read()
batched = batch(content, 6)
res = [dict(emit(b)) for b in batched]

print(res)
