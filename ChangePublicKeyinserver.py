import requests
import os
serveraddr="http://"+input("请输入服务器地址:")+":"+input("请输入服务器端口:")
pw=input("请输入服务器密码:")
e=int(input("请输入公钥:"))
result=requests.post(serveraddr,data={"e":e,"password":pw}).json()
if result["IsThePasswordCorrect"]:
    print("公钥修改成功")
else:
    print("密码错误")

os.system("pause > nul")
