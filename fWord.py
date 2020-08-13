import requests
def getword():
    url="https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn"
    head={}
    head["user-agent"]="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36"
    req = requests.get(url,headers=head)
    data = req.text
    return(data)
if __name__=="__main__":
    print(getword())