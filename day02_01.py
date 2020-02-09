#网站服务器可以看到我们的ip,统一IP不断访问服务器，会被限制，所以要使用IP代理
#系统的urlopen 没有添加代理的功能
#需要我们自定义

import urllib.request

#创建自己的handler
def handler_openner():

    url = "http://www.baidu.com"

    #创建自己的处理器
    handler = urllib.request.HTTPHandler()
    #创建自己的openner
    opener = urllib.request.build_opener(handler)
    
    #用openner调用open方法 请求数据
    response = opener.open(url)
    print(response)
    data = response.read()
    #print(data)


#使用代理
def creat_proxy_handler():
    url = "https://www.baidu.com/"

    #添加代理
    proxy = {
        #免费代理的写法
        #"http":"http://206.189.113.118:8080"
        "http":"194.167.44.91:80"
        #付费
        ##"http":"账号"：密码@ip

    }

    #代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)

    proxy_opener = urllib.request.build_opener(proxy_handler)
    proxy_resopnse = proxy_opener.open(url)
    data1 = proxy_resopnse.read()

    print(data1)


def main():
    handler_openner()
    creat_proxy_handler()

if __name__ == '__main__':
    main()