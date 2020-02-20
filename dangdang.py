import requests
from lxml import etree
import re
import csv

def get_page(key):
    for page in range(1,50):
        url = 'http://search.dangdang.com/?key=%s&act=input&page_index=%s' % (key,page)
        headers = {
            "User_Agent":'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
        }
        free_proxy={
            "http":"61.19.86.221:8080"
        }
        response = requests.get(url = url,headers = headers)#,proxies=free_proxy)
        parse_page(response)
        print('page %s over!!!' % page)

def parse_page(response):
    tree = etree.HTML(response.text)
    li_list = tree.xpath('//ul[@class="bigimg"]/li')
    # print(len(li_list))  # 测试
    for li in li_list:
        data = []
        try:
            # 获取书的标题,并添加到列表中
            title = li.xpath('./p[@class="name"]/a/@title')[0].strip()
            data.append(title)
            # 获取商品链接,并添加到列表中
            commodity_url = li.xpath('./p[@class="name"]/a/@href')[0]
            data.append(commodity_url)
            # 获取价格,并添加到列表中
            price = li.xpath('./p[@class="price"]/span[1]/text()')[0]
            data.append(price)
            # 获取作者,并添加到列表中
            author = ''.join(li.xpath('./p[@class="search_book_author"]/span[1]//text()')).strip()
            data.append(author)
            # 获取出版时间,并添加到列表中
            time = li.xpath('./p[@class="search_book_author"]/span[2]/text()')[0]
            pub_time = re.sub('/','',time).strip()
            data.append(pub_time)
            # 获取评论数,并添加到列表中
            comment_count = li.xpath('./p[@class="search_star_line"]/a/text()')[0]
            # 获取书本的简介,并添加到列表中.由于有些书本没有简介，所以要用try
            commodity_detail = ''
            commodity_detail = li.xpath('./p[@class="detail"]/text()')[0]
            data.append(commodity_detail)
        except:
            pass
        save_data(data)

def save_data(data):
        writer.writerow(data)

def main():
    key = 'python'  # input('Please input key:')
    get_page(key)

fp = open('当当网.csv','w',encoding = 'utf-8-sig',newline = '')
writer = csv.writer(fp)
header = ['标题','链接','价格','作者','出版时间','评论数','简介']
writer.writerow(header)
main()
fp.close()