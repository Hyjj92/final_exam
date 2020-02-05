import urllib.request

def load_data():
    url = "http://www.baidu.com/"

    #response:http请求（request）的响应体
    response = urllib.request.urlopen(url)
    #返回的时response对象   http.client.HTTPResponse object
    print (response)
    
    #读取response的内容 bytes类型
    data = response.read()
    print (data)
    #讲获取内容转换成string
    #encode方法 指定的编码格式编码字符串
    #decode方法 指定的编码格式解码字符串。
    str_data = data.decode("utf-8")
    print (str_data)

    #将数据写入文件
    with open("baidu.html", "w" , encoding = "utf-8" )as f:
       f.write(str_data)

def main():
    load_data()

if __name__ == '__main__':
    main()
      
