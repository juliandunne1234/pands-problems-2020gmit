#Function that writes a dict to a file as JSON
import json

filename="testdict.json"

sample= dict(name='fred', age=31, grades=[1, 43, 55])

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj, f)

writeDict(sample)