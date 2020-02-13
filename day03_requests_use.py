import requests

url = "http://www.baidu.com"

response = requests.get(url)

#content属性 返回的时字节
data = response.content
data1 = response.content.decode("utf-8")

print(response)
print(type(data))   #byte
print(type(data1))  #str
print(data)
print(data1)

#text返回的时文本 str  对二进制文件的编码方式的确定 采用 猜的方式  一般都对 
data = response.text
print(data)
