import os
import requests
import unicode
import rsa
e=input("请输入公钥指数(输入s则从服务器获取):")
n=input("请输入公钥模数(输入s则从服务器获取):")

def cls():
    os.system("cls")
serverip=input("请输入服务器的ip(默认本机ip):")
if serverip=='':
    serverip='127.0.0.1'

serverport=input("请输入服务器的端口:")
serveraddress="http://"+serverip+":"+serverport
if requests.get(serveraddress).json()=='Chat Server(Status Code:200)':
    if e=='s' or n=='s':
        if e=='s':
            e=requests.post(serveraddress,data={"viewe":1}).json()["e"]
        else:
            e=int(e)
        if n=='s':
            n=requests.post(serveraddress,data={"viewn":1}).json()["n"]
        else:
            n=int(n)
    rsa.__prep(e,n)
    name=input("请输入你的昵称:")
    while True:
        msg=input("请输入消息(输入quit退出程序):")
        if msg.lower()=="quit":
            break
        requests.post(serveraddress,data={"message":str(rsa.encryptls(unicode.encode(name+":"+msg)))})
        cls()
