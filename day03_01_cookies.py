import urllib.request
from http import cookiejar
from urllib import parse 


#手动粘贴cookies
def Manual_cookies():
    url = "https://i.taobao.com/my_taobao.htm?spm=a21bo.2017.1997525045.1.5af911d9RqvZFl"

    header ={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
        ,
        "Cookie":"BAIDUID=09D4656F084B89A16102A8E7E209B101:FG=1; PSTM=1554894131; BIDUPSID=6AF1A393AFAA81A582F2C8557A788C05; HMACCOUNT=D2E2BEA1282959AB; BDUSS=ZYMFJiemRKfmtZZXB6d1pCWDB6VTVCZzRJfnBoNTVxcU5LZHd0LXNoSHF4aXRlSVFBQUFBJCQAAAAAAAAAAAEAAAAtPoZ2cmVuc2hlbmdlMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOo5BF7qOQReQl; BDRCVFR[2eykiTybMOm]=mk3SLVN4HKm; H_PS_PSSID=; delPer=0; PSINO=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0"
    }
    request = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(request)

    data = response.read()
    print("0000")

    with open("cookies01.html","wb")as c:
        c.write(data)


def automatic_cookies():
    """
    代码登录，登陆成功后自动去请求个人中心

    cookiejar 自动保存cookie
    """
#后台根据你发送的请求方式来判断的
#如果你是get  返回来的时 登录页面    如果是POST  返回的时登陆结果
#1、代码登录
    #网址，参数，登录请求post
    login_url = "https://www.yaozh.com/login/"
    login_form_data = {
        "username":"Hyjj92",
        "pwd":"Wo15951000937",
        "formhash":"3B3AB8F5CA",
        "backurl":"https%3A%2F%2Fwww.yaozh.com%2F"
        }
    cook_jar = cookiejar.CookieJar()
    cook_handler = urllib.request.HTTPCookieProcessor(cook_jar)
    opener = urllib.request.build_opener(cook_handler)
    header = {
        "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
    }
    login_str = urllib.parse.urlencode(login_form_data).encode("utf-8")
    login_resquest = urllib.request.Request(login_url,data=login_str,headers=header)
    #登陆成功 cook jar自动保存cookie
    opener.open(login_resquest)

#2、带着cookie访问个人中心
    center_url = "https://www.yaozh.com/member/"
    center_request = urllib.request.Request(center_url,headers=header)
    response = opener.open(center_request)
    data = response.read()

    with open("cookie02.html","wb")as f:
        f.write(data)



def main():
    #Manual_cookies()
    automatic_cookies()

if __name__ == '__main__':
    main()
