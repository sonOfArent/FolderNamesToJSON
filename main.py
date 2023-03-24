import os
import json

namesDict = {}

folder_dir = './images'
for image in os.listdir(folder_dir):
    namesDict[image[:-4]] = image

namesDictJSON = json.dumps(namesDict)

f = open("namesdata.json", "x")
f.write(namesDictJSON)
f.close()

f = open("namesdata.json", "r")
print(f.read())
f.close()