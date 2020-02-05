import urllib.request
import urllib.parse
import string

#传一个参数
def get_method_param():
    url = "http://www.baidu.com/s?wd="
    #拼接字符串
    name = "科比"
    final_url = url + name
    print(final_url)

    #python解析器只支持ASCII码  不支持中文
    #将包含汉字的 一个字符串 转义
    new_final_url = urllib.parse.quote(final_url,safe = string.printable)
    print(new_final_url)

    #发送网络请求
    response = urllib.request.urlopen(new_final_url)
    print(response)

    #读取内容
    data = response.read().decode()
    print(data)

    with open("02.html", "w" , encoding = "utf-8" )as f:
       f.write(data)


#传多个参数
def get_method_params():
    url =  "http://www.baidu.com/s?"

    params = {
        'wd':'中文',
        "key":"aaaa",
        'value':'san'
    }

    #将字典里面所有的键值转化为query-string格式（key=value&key=value），并且将中文转码
    str_params = urllib.parse.urlencode(params)
    print(str_params)   #wd=%E4%B8%AD%E6%96%87&key=aaaa&value=san

    final_url = url + str_params

    response = urllib.request.urlopen(final_url)
    data = response.read().decode()
    print(data)

    with open("03.html",'w',encoding="utf-8") as f:
        f.write(data)




def main():
    get_method_param()
    get_method_params()

if __name__ == '__main__':
    main()