import requests
from time import sleep
import unicode
import rsa
import os
d=int(input("请输入私钥:"))
n=int(input("请输入公钥模数:"))
rsa.__prep(_d=d,_n=n)
os.system("cls")

chatls=[]
newmsg=[]
serverip=input("请输入服务器的ip(默认本机ip):")
if serverip=='':
    serverip='127.0.0.1'

serverport=input("请输入服务器的端口:")
serveraddress="http://"+serverip+":"+serverport
if requests.get(serveraddress).json()=='Chat Server(Status Code:200)':
    while True:
        ls=requests.post(serveraddress,data={"viewcl":"1"}).json()
        newmsg=ls[:]
        if ls!=chatls:
            for i in chatls:
                newmsg.remove(i)
            chatls.extend(newmsg)
            for i in newmsg:
                msgls=eval(i)
                d=unicode.decode(rsa.decryptls(msgls))
                print(d)
        sleep(1)
