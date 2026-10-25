import json
import requests
import os
jsonurl='https://dl.google.com/dl/edgedl/chromeos/recovery/recovery.json'
localjson=requests.get(jsonurl).content
buildlist=json.loads(localjson)
try:
    board=os.environ.get("chromeos_dlboard")
except:
    pass
if board is None:
    board='jinlon'
builds=[b for b in buildlist if(b.get("hwidmatch").__contains__(board) or (b.get("hwidmatch").__contains__(board.upper())))]
display=[]
builddata=''
for b in builds:
    for attrib in ['manufacturer','model','channel','version','chrome_version','hwidmatch','url']:
        dispattr =b.get(attrib)
        if (dispattr == "null"):
            dispattr="unknown"
        builddata=(builddata+"\t"+dispattr)
    display.append(builddata)
    builddata=''
selected=None
dlindex=os.environ.get("chromeos_dlindex")
try:
    selected=display[int(dlindex)].split("\t")[-1]
except:
    dlindex=None
while(dlindex is None):
    for d in display:
        print(str(display.index(d))+d)
    try:
        dlindex=input()
        selected=display[int(dlindex)].split("\t")[-1]
        break
    except:
        continue
print(selected)
