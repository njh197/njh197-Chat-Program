import rsa
import os
import requests
try:
    p=int(input("输入第一个数:"))
    q=int(input("输入另一个比第一个大的数:"))
    bigger={"y":True,"n":False}[input("是否需要更大的公钥?(y/n):").lower()]
    rsa.prep(p,q,bigger=bigger)
    if rsa.encrypt(rsa.decrypt(114))==114:
        print("你的公钥:",rsa.e)
        print("你的公钥模数:",rsa.n)
        print("你的私钥:",rsa.d)
        choice=input("是否将公钥发送到服务器保存?(y/n)")
        if choice.lower()=="y":
            serveraddr="http://"+input("请输入服务器ip地址:")+":"+input("请输入服务器开放端口:")
            pw=input("请输入服务器密码:")
            if requests.post(serveraddr,data={"e":rsa.e,"password":pw}).json()["IsThePasswordCorrect"]:
                requests.post(serveraddr,data={"n":rsa.n,"password":pw})
                print("请求发送成功")
            else:
                print("密码不正确")
    else:
        print("生成失败")
    os.system("pause > nul")
except Exception as err:
    print("错误:",err)
    os.system("pause > nul")
