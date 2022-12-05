import requests
from time import sleep
import unicode
import rsa
import os
try:
    d=int(input("请输入私钥:"))
    n=input("请输入公钥模数(输入s则从服务器获取):")
    os.system("cls")

    chatls=[]
    newmsg=[]
    serverip=input("请输入服务器的ip(默认本机ip):")
    if serverip=='':
        serverip='127.0.0.1'

    serverport=input("请输入服务器的端口:")
    serveraddress="http://"+serverip+":"+serverport
    if requests.get(serveraddress).json()=='Chat Server(Status Code:200)':
        if n=='s':
            n=requests.post(serveraddress,data={'viewn':1}).json()["n"]
        else:
            n=int(n)
        rsa.__prep(_d=d,_n=n)
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
except Exception as err:
    print("错误:",err)
    os.system("pause > nul")
