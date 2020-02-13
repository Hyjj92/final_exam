#urllib.request  提示错误  httperror   urlerror

import urllib.request

#urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
url = "http://www.sasdass.com"
response = urllib.request.urlopen(url)

#urllib.error.HTTPError: HTTP Error 404: Not Found
url = "https://blog.csdn.net/xixi880928/article/details/120"
response = urllib.request.urlopen(url)