import os
import time
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests   
def getword():
    head={}
    head["user-agent"]="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36"
    req = requests.get(url,headers=head)
    data = req.text
    return(data)
if __name__=="__main__":
    url="https://zuanbot.com/api.php?level=min&lang=zh_cn"
    for i in range(100):
        print(getword())
        time.sleep(0.5)
    input("Press entry to close")    
