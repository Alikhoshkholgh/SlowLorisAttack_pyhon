# SlowLorisAttack_pyhon
this script create several tcp-sessions(with multiple threads) and send HTTP-GET request to the target machine

+ RUN:
    + python ./driver.py
    
    
    
+ About ./driver.py Code Variables:

    + target :  target IP address
    + port:     target port number
    + connection_count: how many connections do you want this script to create and then send GET requests
    + timeInterval: at which time interval do you want this script to send GET requests
    + uri: specify the uri you want to request for
