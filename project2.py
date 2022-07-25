from msilib.schema import Error
import os
from sqlite3 import connect
from unittest import result
from ipaddress import ip_address
import socket
import sys
import time
import socket
import base64
class device:
    counter=0
    def __init__(self,ip,mac,name):
        self.ip=ip
        self.mac_addres=mac
        self.name=name
        device.counter=+1
        try:
            iplist=['8.8.8.8']
            for ip in iplist:
                self.result=result
                response=os.popen(f"ping {self.ip}").read()
                if "recieved==4" in response:
                    print(f"up{self.ip} ping successfully")
                    return result=="succesful"
                    
                else:
                    print(f"down {self.ip}ping successfully")
        except:
            print(EnvironmentError)
        
            
    def status(self):
        if result=="succesful" :
            return self.status==1
        else:
            return self.status==0 

def connecttotv(hostname):
    ip=socket.gethostbyname(hostname)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port=80
    s.connect((ip,port))
    msg=s.recv(1024)
    print(msg.decode("utf-8"))
    print(f'Socket has successfully connected to github on port =={ip}')
        

def ip(a):
    a= input("Please enter the router Ip: ")
    return a
def getting_Ip(hostname):
    ip=socket.gethostbyname(hostname)
    print("IP Address is: %s " %ip )
connecttotv('www.github.com')

