import rsa
import os
p=int(input("输入第一个数:"))
q=int(input("输入另一个比第一个大的数:"))
bigger={"y":True,"n":False}[input("是否需要更大的公钥?(y/n):").lower()]
rsa.prep(p,q,bigger=bigger)
if rsa.encrypt(rsa.decrypt(114))==114:
    print("你的公钥:",rsa.e)
    print("你的公钥模数:",rsa.n)
    print("你的私钥:",rsa.d)
else:
    print("生成失败")
os.system("pause > nul")
