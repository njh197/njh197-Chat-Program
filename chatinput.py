import os
import requests
import unicode
import rsa
e=int(input("请输入公钥指数:"))
n=int(input("请输入公钥模数:"))
rsa.__prep(e,n)
def cls():
    os.system("cls")
serverip=input("请输入服务器的ip(默认本机ip):")
if serverip=='':
    serverip='127.0.0.1'

serverport=input("请输入服务器的端口:")
serveraddress="http://"+serverip+":"+serverport
if requests.get(serveraddress).json()=='Chat Server(Status Code:200)':
    while True:
        msg=input("请输入消息(输入quit退出程序):")
        if msg.lower()=="quit":
            break
        requests.post(serveraddress,data={"message":str(rsa.encryptls(unicode.encode(msg)))})
        cls()
