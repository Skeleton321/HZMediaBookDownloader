from http.server import HTTPServer,BaseHTTPRequestHandler,HTTPStatus
from threading import Lock
import random
from io import BytesIO
import numpy  as np
host = ("localhost",8899)
data = []
back_data = {}
n = 5   #一次发送的任务个数
lock = Lock()
class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        global data
        global back_data
        global lock
        respone_text = ""
        lock.acquire()
        if self.path == "/gettask":
            try:
                for i in range(n):
                    #按照优先级获取任务
                    d = data.pop(0)
                    respone_text += str(d) + " "
                    back_data.update({d:d}) #标记已发送的任务，如果用户下载完成并且传回任务，这个字典里的书籍id会被删除
            except:
                respone_text = "clear"

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes(respone_text,encoding="utf8"))
        lock.release()
    def saveFile(self,content,name):
        with open(name,"wb") as f:
            f.write(content)

    def do_POST(self):
        if self.path == "/senddata":
            global lock
            global back_data
            lock.acquire()
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            #back_data.pop(body)
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(bytes("OK",encoding="utf8"))
            lock.release()
#data = list(np.random.random_integers(1,100000,size=1400))
server = HTTPServer(host,Request)
server.serve_forever()
