"""关于RSA加密的简单lib"""
n,e,d=0,0,0 #p和q是两个质数,N是p*q(公钥模数),T是(p-1)*(q-1),E是公钥,D是私钥
class RSAError(Exception): #RSA错误
    pass

def isprime(num): #判断质数
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def _prep(p,q,_e,skipEcheck=False):
    global n,e,d
    n=p*q
    t=(p-1)*(q-1)
    #下面代码检测E是否符合规定
    #公钥E需要不是t的因子,1<e<t,而且E是质数
    if not skipEcheck:
        if isprime(_e):
            if 1<_e and _e<t:
                if t%_e!=0:
                    e=_e
                else:
                    raise RSAError("公钥E不是(p-1)*(q-1)的因子")
            else:
                raise RSAError("1<公钥E<(p-1)*(q-1)")
        else:
            raise RSAError("公钥E是质数")
    else:
        e=_e
    cnt=0
    i=0
    while cnt<=1:
        if (i*e)%t==1:
            cnt+=1
            d=i
        i+=1

def __prep(_e=0,_n=0,_d=0):
    global e,n,d
    e=_e
    n=_n
    d=_d

def encrypt(a): #加密
    return a**e%n

def encryptls(a):
    return [encrypt(i) for i in a]

def decryptls(a):
    return [decrypt(i) for i in a]

def decrypt(a): #解密
    return a**d%n

def _prime1(a,b):
    for i in range(a,b+1):
        if isprime(i):
            return i

def _prime2(a,b):
    for i in range(b,a-1,-1):
        if isprime(i):
            return i

def pq(a,b): #求p和q的函数,a<b,a和b是范围
    return [_prime1(a,b),_prime2(a,b)]

def generate_e(p,q,bigger=True):
    t=(p-1)*(q-1)
    if bigger:
        for i in range(t,0,-1):
            if isprime(i) and t%i!=0:
                return i
    else:
        for i in range(1,t+1):
            if isprime(i) and t%i!=0:
                return i
        return -1

def prep(a,b,bigger=True): #a~b:范围 值别太小(也别太大)！
    ls=pq(a,b)
    p_=ls[0]
    q_=ls[1]
    e_=generate_e(p_,q_,bigger=bigger)
    if e_==-1:
        raise RSAError("没有找到可用的公钥")
        return None
    else:
        _prep(p_,q_,e_)

if __name__=='__main__':
    _prep(3,11,3)
    print("test 1 prepare OK")
    print(e)
    assert 14==decrypt(encrypt(14))
    print("test 1.1 OK")
    assert [13,25]==decryptls(encryptls([13,25]))
    print("test 1.2 OK")
    prep(143,999,bigger=True)
    print("test 2 prepare OK(E="+str(e)+")")
    assert 14==decrypt(encrypt(14))
    print("test 2.1 OK")
    assert [13,25]==decryptls(encryptls([13,25]))
    print("Test 2.2 OK")
