from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import json
import os
import hashlib
#部分代码来源：https://blog.csdn.net/qq_21420855/article/details/123086661
e=0
n=0
chatls=[]
password=hashlib.md5(bytes(input("输入密码:")+"IsThePassword",encoding='utf8')).hexdigest()
os.system("cls")
class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path, args = urllib.parse.splitquery(self.path)
        self._response(path, args)
 
    def do_POST(self):
        args = self.rfile.read(int(self.headers['content-length'])).decode("utf-8")
        self._response(self.path, args)
 
    def _response(self, path, args):
        global e,n
        # 组装参数为字典
        if args:
            args = urllib.parse.parse_qs(args).items()
            args = dict([(k, v[0]) for k, v in args])
        else:
            args = {}
        # 设置响应结果
        argskeys=list(args.keys())
        if sorted(argskeys)==sorted(['e','password']):
            if hashlib.md5(bytes(args['password']+"IsThePassword",encoding='utf8')).hexdigest()==password:
                e=int(args["e"])
                result={"status":200,"IsThePasswordCorrect":True}
                print("有人把公钥E修改为了"+str(e))
            else:
                print("有人试图把公钥E修改为"+str(args['e'])+",但是他的密码不正确")
                result={"status":200,"IsThePasswordCorrect":False}
        elif sorted(argskeys)==sorted(['n','password']):
            if hashlib.md5(bytes(args['password']+"IsThePassword",encoding='utf8')).hexdigest()==password:
                n=int(args["n"])
                result={"status":200,"IsThePasswordCorrect":True}
                print("有人把公钥模数N修改为了"+str(n))
            else:
                print("有人试图把公钥模数N修改为"+str(args['n'])+",但是他的密码不正确")
                result={"status":200,"IsThePasswordCorrect":False}
        elif argskeys==['viewe']:
            result={"e":e,"status":200}
        elif argskeys==['viewn']:
            result={"n":n,"status":200}
        elif argskeys==['message']:
            print("有人发送了消息:"+args['message'])
            chatls.append(args['message'])
            result={"status":200}
        elif argskeys==['viewcl']:
            result=chatls
        else:
            result='Chat Server(Status Code:200)'
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode()) 
 
if __name__ == '__main__':
    try:
        # 开启http服务，设置监听ip和端口
        port=input("输入开放端口(默认8787):")
        if port=="":
            port=8787
        else:
            port=int(port)
        print("正在启动服务器")
        httpd = HTTPServer(('', port), HttpHandler)
        os.system("cls")
        print("HTTP服务器启动成功(端口"+str(port)+")")
        httpd.serve_forever()
    except Exception as err:
        print("错误:",err)
    finally:
        os.system("pause > nul")
