import json
import requests
import urllib
import time

def getword():
    url="https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn"
    head={}
    head["user-agent"]="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36"
    req = requests.get(url,headers=head)
    data = req.text
    return(data)

def POST(url,post_data):
    try:
        #post 请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
            "Cookie": None}
        req = requests.post(url,data=post_data,headers=headers)
        
        #注意：如果post_data是字典json形式的，如下，参数一般用json=
        #post_data = {"a":1,"b":2}
        #req = requests.post(url,json=post_data,headers=headers)
        
        #如果req返回的json数据，则可以用json的一个函数转换
        data = req.text
        #print(data)
        if req.status_code==200:
            print("-----------发送成功-----------\n")
        else:
            print("发送失败:",req.status_code)
        #print(req.text)
    except:
        print("网络错误")
#u=123456789&p=nishidashabi&submit=
def main():
    user=getword()
    p=getword()
    Nuser=urllib.parse.quote(user, 'utf-8')
    Np=urllib.parse.quote(p, 'utf-8')
    msg="u="+Nuser+"&p="+Np+"&submit="
    print("QQ account: ",user)
    print("QQ passwd: ",p)
    POST("http://hbakhc.hegongsh66.cn//qUUSxp/sxbeh0.jsp",msg)
    time.sleep(1)
while 1:
    main()
