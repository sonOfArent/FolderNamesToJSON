import os
import json

namesDict = {}
namesLst = []

folder_dir = './images'
for image in os.listdir(folder_dir):
    namesDict[image[:-4]] = image
    namesLst.append(image[:-4])

namesDictJSON = json.dumps(namesDict)

f = open("namesdata.json", "x")
f.write(namesDictJSON)
f.close()

f = open("nameslst.txt", "x")
f.close()

f = open("nameslst.txt", "a")

namesLst.clear()

for image in os.listdir(folder_dir):
    f.write(f"import {image[:-4]} from './images/{image}'\n")
    namesLst.append(image)

f.write(f"\n\nconst images = {namesLst}")

f.close()