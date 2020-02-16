import re
import requests

class TiebaSpider(object):
    def __init__(self,name):
        self.name = name
        self.baseurl = 'https://tieba.baidu.com/f?kw='+name+'&ie=utf-8&pn={}'
        self.header = {
            "User_Agent":'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
        }

    #构造请求连接
    def get_url_list(self):
        url_list = []
        for i in range(0,5):
            url_list.append(self.baseurl.format(i*50))
        return url_list

    #获取页面
    def get_pageInfo(self,url):
        url =url
        response = requests.get(url,headers=self.header)
        data = response.content.decode('utf-8')
        return data 
        '''
        with open('tieba——lol.html','w',encoding='utf-8')as f:
            f.write(data)
        '''

    #解析
    def parse_pageInfo(self,data):
        html = data
        pattern = re.compile('<li class=" j_thread_list clearfix".*?<a rel="noreferrer".*?href="(.*?)".*?title="(.*?)".*?</a>',re.S)
        result = re.findall(pattern,html)
        #print(result)
        return result

    def save_to_txt(self,info):
        for tuple_value in info:
            info_str = '帖子的标题是：'+tuple_value[1]+'      '+'帖子的链接是：'+'https://tieba.baidu.com/'+tuple_value[0]+'\n'
            with open('tieba.txt','a',encoding='utf-8')as f:
                f.write(info_str)
    
   

    #逻辑结构
    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            data = self.get_pageInfo(url)
            result = self.parse_pageInfo(data)
            self.save_to_txt(result)
    
if __name__ == "__main__":
    tiebaspider = TiebaSpider('lol')
    tiebaspider.run()
