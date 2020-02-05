import urllib.request
import random 


#使用多个 UA 抓取
def load_baidu_nUA():

    User_agent_list = [
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    ]
    url = "http://www.baidu.com"

    random_ua = random.choice(User_agent_list)

    #获得request对象，添加请求头信息，请求数据
    request = urllib.request.Request(url)
    request.add_header("User-Agent",random_ua)
    response = urllib.request.urlopen(request)

    print(request.get_header("User-agent") )


def main():
    load_baidu_nUA()

if __name__ == '__main__':
    main()