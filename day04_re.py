import re
"""
re.compile 用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，
re_basics():
re_function()
re_split()
re_ chinese()
"""



def re_basics():
    one = "masdfghn12345n"
    #贪婪模式  默认
    #. 任意  * 任意次
    pattern = re.compile('m(.*)n')
    result = pattern.findall(one)
    print(result)

    pattern = re.compile('m(.*?)n')
    result = pattern.findall(one)
    print(result)

    #. 不能匹配换行 \n  加参数 re.s后 可以  re.I 忽略大小写
    one = """masdfghn
    12345n
    12345N
    """
    pattern = re.compile('m(.*)n',re.S|re.I)
    result = pattern.findall(one)
    print(result)

def re_function():
    one = "asd123"
    two = "123asd"
    pattern = re.compile('\d+')
    #match 冲头匹配  匹配一次
    result = pattern.match(one)
    print(result)
    result = pattern.match(two)
    print(result)
    #search 从任意位置 匹配一次
    result = pattern.search(one)
    print(result)
    result = pattern.search(two)
    print(result)
    #findall 查找符合 正则的内容  --list
    result = pattern.findall(one)
    print(result)

    #sub 替换字符串
    result = pattern.sub('*',one)
    print(result)

    #spilt 拆分
    three = "123 asd"
    pattern = re.compile(" ")
    result = pattern.split(three)
    print(result)

def re_split():
    one = "aaaszzsxxsccccccsvvvvs"
    #拆分标准  s
    patter = re.compile('s')
    result = patter.split(one)
    print(result)

def re_chiunese():
    one = '<input class="placeholder" placeholder="搜索...大撒大撒" name="s" autocomplete="off">'
    patter = re.compile('[\u4e00-\u9fa5]')
    result = patter.findall(one)
    print(result)
    patter = re.compile('[\u4e00-\u9fa5]+')
    result = patter.findall(one)
    print(result)


    

def main():
    #re_basics()
    #re_function()
    #re_split()
    re_chiunese()

if __name__ == '__main__':
    main()