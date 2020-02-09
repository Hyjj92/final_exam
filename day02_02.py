import urllib.request

def proxy_user():

    url = "http://www.baidu.com/"
    proxy_list = [
        {"http":"206.189.113.118:8080"},
        {"http":"194.167.44.91:80"},
        {"http":"103.106.1.110:8080"},
        {"http":"45.232.244.41:8080"},
        {"http":"62.176.12.111:8080"},
        {"http":""}
    ]

    for proxy in proxy_list:
        print(proxy)
        proxy_handler = urllib.request.ProxyHandler(proxy)
        proxy_opener = urllib.request.build_opener(proxy_handler)

        #在使用免费代理时对代理不能用的处理
        try:
            proxy_opener.open(url,timeout=1)
            print("...........")
        except Exception as e:
            print(e)

def main():
    proxy_user()

if __name__ == '__main__':
    main()