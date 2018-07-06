import json
import sys
import glob

# first argument provides the hash name
id = sys.argv[1]

#open base model file and read the JSON object
f = open(id + "/model0", 'r')
model = json.load(f.read())

annotations = glob.glob('annotation*.json')
for a in annotations:
    nf = open(a,'r')
    annotation = nf.read()
    
    for part in model:
        if annotation["body"]["type"] == "volume":
            part["gain"] += annotation["body"]["type"]
        elif annotation["body"]["type"] == "time":
            part["gain"] += annotation["body"]["type"]

        model = part
        outf = open("out+a, 'w')
        outf.write(model)
