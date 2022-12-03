def encode(s):
    e=[ord(i) for i in s]
    return e
def decode(s):
    return "".join([str(chr(i)) for i in s])

if __name__=='__main__':
    print(encode("abc"))
    print(decode(encode("qwe")))
    print(decode([97,97,97]))
