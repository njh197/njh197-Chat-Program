import rsa
import os
p=int(input("输入第一个质数:"))
q=int(input("输入另一个比第一个大的质数:"))
rsa.prep(p,q)
if rsa.encrypt(rsa.decrypt(114))==114:
    print("你的公钥:",rsa.e)
    print("你的公钥模数:",rsa.n)
    print("你的私钥(别告诉别人):",rsa.d)
else:
    print("生成失败")
os.system("pause > nul")
