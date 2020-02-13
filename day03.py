import requests

#url = "http://www.baidu.com/s?wd=谷歌"

url = "http://www.baidu.com/s"
params = {
    "wd":"谷歌"
}
header = {
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1"
}

response = requests.get(url, headers=header,params=params)
data = response.content.decode("utf-8")

with open ("baidu.html","w",encoding="utf-8") as f:
    f.write(data)

