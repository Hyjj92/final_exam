import urllib.request
import urllib.parse
import string

#构建自己的请求头

def load_baidu():
    url = "http://www.baidu.com"
    
    #添加请求头信息
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
    }
    #创建 指定url的请求对象，添加ua
    request = urllib.request.Request(url,headers=header)

    request = urllib.request.Request(url)
    #动态添加UA
    #request.add_header("User-agent","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")

    #请求网络数据
    respons = urllib.request.urlopen(request)
    data = respons.read().decode("utf-8")
    with open("hesders.html","w",encoding="utf-8")as f:
        f.write(data)

    #响应头
    #print(respons.headers)
    #注意，要求首字母大写，其它字母小写
    request_header = request.get_header("User-agent")
    print(request_header)
    #获取完整的url
    final_url = request.get_full_url()
    print(final_url)


def main():
    load_baidu()

if __name__ == '__main__':
    main()