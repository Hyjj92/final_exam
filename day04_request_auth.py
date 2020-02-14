import requests
#发送post
url = ""
data = {
    "":""
}
response = requests.post(url,data=data)

#auth  n内网 需要认证
user = ""
psw = ""
auth = {user,psw}
response = requests.get(url,auth=auth)
