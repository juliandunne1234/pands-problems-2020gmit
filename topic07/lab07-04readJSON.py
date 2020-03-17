#Function that reads a dict from a JSON file
import json

filename="testdict.json"

def readDict():
    with open(filename) as f:
        return json.load(f)

somedict = readDict()
print(somedict)