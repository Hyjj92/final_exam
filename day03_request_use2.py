import requests

class RequestSpider(object):
    def __init__(self):
        url = "http://www.baidu.com"
        header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
        }
        self.response = requests.get(url, headers=header)
    
    def run(self):
        data = self.response.content

        #请求头 响应头
        request_headers = self.response.request.headers
        #print(request_headers)
        response_headers = self.response.headers
        #print(response_headers)

        #响应状态码
        code = self.response.status_code
        print(code)

        #请求的cookie  相应的cookie
        request_cookie = self.response.request._cookies
        print(request_cookie)

        response_cookie = self.response.cookies
        print(response_cookie)

RequestSpider().run()