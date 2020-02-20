# final_exam
python期末考核  
学号：1120190807  姓名：戴智文

其中day01--day04的内容是学习部分。dangdang.py是提交的作业。当当网.csv是测试结果。

关于dangdang.py

1、目标
    爬取当当网上，以python为关键字的书籍的信息。（这里只获取了前49页）

2、提取的信息
    ①标题  ②链接  ③价格  ④作者  ⑤出版时间  ⑥评论数  ⑦简介

3、开发环境和技术选择
    开发语言：python3
    爬虫技术：requests第三方模块
    存储：存储在 .csv文件中

4、实现
    get_page(key)  获取网页的页面信息  （使用了User-Agent，和IP代理，因为使用的是免费IP代理有可能失效，故在测试后注释掉）
    parse_page(response)  解析获取的页面
    save_data(data) 保存数据
    
    
