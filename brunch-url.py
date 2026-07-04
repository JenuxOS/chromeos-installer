import json
import requests
import sys
try:
    repo=sys.argv[1]
    assetindex=sys.argv[2]
except:
    print("usage: "+sys.argv[0]+" <owner/repo> <0 based index of asset>")
    sys.exit(2)
releasedata=[]
urls=[]
newjson={}
page=1
per_page=30
while 1:
    baseurl="https://api.github.com/repos/"+repo+"/releases?per_page="+str(per_page)+"&page="+str(page)
    newjson=(json.loads(requests.get(baseurl).content))
    if(len(newjson)>0):
        for i in newjson:
            for j in i.get("assets"):
                urls.append(j.get("browser_download_url"))
        page=(page+1)
        continue
    else:
        break
try:
    url=urls[int(assetindex)]
except IndexError:
    print("Selected asset not found.")
    sys.exit(4)
print(url)
