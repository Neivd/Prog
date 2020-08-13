import requests
import json
#ocqZ7AsFpWBXE6WciY4X
header={"token":"ocqZ7AsFpWBXE6WciY4X"}
url= "https://v1.alapi.cn/api/new/wbtop"
result=requests.post(url,headers=header)
text=json.loads(result.text)
#print(text)
print("Weibo hot word")
for i in text["data"]:
    print(i["hot_word"],i['hot_word_num'])
input("Press Enter to Close")