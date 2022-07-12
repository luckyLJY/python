## 正则表达式
基本元字符:   
字符转义:\w+，\.   
![](./img/%E5%9F%BA%E6%9C%AC%E5%AD%97%E7%AC%A6.png)
```python
示例代码如下：
# coding=utf-8 
＃代码文件：chapterl4/chl4.l.3.py
import re 
pl= r'＼w+@zhijieketang\.com' 
p2 = r'＼w+@zhijieketang\.com$'

text = "Tony's email is tony_guan588@zhijieketang.com."
m = re.search(p1,text)
print(m)

m = re.search(p2,text)
print(m)

email = 'tony_guan588@zhijieketang.com'
m = re.search(p2,email)
print(m)
```

#### 字符类
1. 定义字符类
    ```python
    import re
    p = r'[Jj]ava'
    m = re.search(p,'I like Java and Python.')
    print(m) #匹配
    m = re.search(p,'I like JAVA and Python.')
    print(m) #不匹配
    m = re.search(p,'I like java and Python.')
    print(m) #匹配
    ```

2. 字符类取反
    ```python
    import re
    p = r'[^0123456789]'
    m = re.search(p,'1000')
    print(m) # 不匹配
    m = re.search(p,'Python 3')
    print(m) #匹配
    ```
3. 区间  
[0123456789] == [0-9]  
[^0123456789] == [^0-9]  
[a-z]   
[A-Z]
4. 预定义字符类
![](./img/%E9%A2%84%E5%AE%9A%E4%B9%89%E5%AD%97%E7%AC%A6%E7%B1%BB.png)
    ```python
    import re
    p = r'\D'

    m = re.search(p,'1000'0)
    print(m) # 不匹配

    m = re.search(p,'Python 3')
    print(m) #匹配

    text = '你们好Hello'
    m = search(r'\w',text)
    print(m)# 匹配
    ```
#### 量词
1. 量词的使用  
    ```txt
    ？   出现零次或一次
    *    出现零次或多次
    +    出现一次或多次
    {n}  出现n次
    {n,m} 至少出现n次但不超过m次
    {n,}  至少出现n次
    ```
    ![](./img/%E9%87%8F%E4%BD%BF%E7%94%A8.png)
2. 贪婪量词和懒惰量词  
    ```python
    import re
    # 使用贪婪量词:尽可能多的匹配字符
    m = re.search(r'\d{5,8}','87654321')
    print(m) #87654321

    # 使用惰性量词：尽可能少的匹配字符
    m = re.search(r'\d{5,8}?','87654321')
    print(m) #87654
    ```
#### 分组
1. 分组使用
    ```python
    import re
    p = r'(121){2}'
    m = re.search(p,'121121abcabc')
    print(m) #匹配
    print(m.group())# 返回匹配字符串
    print(m.group(1))# 获取第一组内容

    p = r'(\d{3,4})-(\d{7,8})'
    m = re.search(p,'010-87654321')
    print(m) # 匹配
    print(m.group()) # 返回匹配字符串
    print(m.groups()) # 获得所有组内容
    ```
2. 分组命名  
```python
import re

p = r'(?P<area_code>\d{3,4})-(?P<phone_code>\d{7,8})'  
m = re.search(p,'010-87654321')
print(m) # 匹配
print(m.group()) # 返回匹配字符串
print(m.groups())# 获得所有组内容

# 通过组编号返回组内容
print(m.group(1))
print(m.group(2))

# 通过组名返回组内容
print(m.group('area_code'))
print(m.group('phone_code'))
```
3. 反向引用分组
```python
import re
# p = r'<([\w]+)>.*</([\w]+)>'
p = r'<([\w]+)>.*</\1>' # 使用反向引用

m = re.search(p,'<a>abc</a>')
print(m) # 匹配

m = re.search(p,'<a>abc</b>')
print(m) # 匹配

```
4. 非捕获分组
    ```python
    import re
    s = 'img1.jpg,img2.jpg,img3.bmp'  

    # 捕获分组
    p = r'\w+(?:\.jpg)'
    mlist = re.findall(p,s)
    print(mlist)

    # 非捕获分组
    p = r'\w+(?:\.jpg)'
    mlist = re.findall(p,s)
    print(mlist)
    ```
#### re模块
1. search()和match()函数
    - search()在输入字符串中查找，返回第一个匹配内容，如果找到一个则match对象，如果没有找到返回None。  
    - match()在输入字符串开始处查找匹配内容，如果找到一个则match对象，如果没有找到返回None。   
2. findall()和finditer()函数
    - findall():在输入字符串中查找所有匹配内容，如果匹配成功，则返回match列表对象，如果匹配失败则返回None。  
    - findfilter():在输入字符串中查找所有匹配内容，如果匹配成功，则返回内容纳math的可迭代对象，同迭代对象每次可以返回一个match对象，如果匹配失败则返回None。
3. 字符串分隔  
    re.split(pattern,string,maxsplit=0,flags=0)   
    pattern:正则表达式；   
    string:要分隔的字符串；  
    maxsplit:最大分隔次数；  
    flags:编译标志；  
    
    ```python
    import re
    p = r'\d+'
    text = 'AB12CD34EF'

    clist = re.split(p,text)
    print(clist)

    clist = re.split(p,text,maxsplit=1)
    print(clist)

    clist = re.split(p,text,maxsplit=2)
    print(clist)
    ```
4. 字符串替换
    re.sub(pattern,repl,string,count=0,flags=0)   
    pattern:正则表达式  
    repl:替换字符串  
    string:要提供的字符串  
    count:要替换的最大数量，默认为零，表示替换数量没有限制   
    flags:编译标志  

     ```python
    import re
    p = r'\d+'
    text = 'AB12CD34EF'

    repace_text = re.sub(p,' ',text)
    print(repace_text)

    repace_text = re.sub(p,' ',text, count=1)
    print(repace_text)

    repace_text = re.sub(p,' ',text,count=2)
    print(repace_text)
    ```
#### 编译正则表达式
1. 已编译正则表达式对象  
re.compile(pattern[,flags=0])  
![](./img/%E5%B7%B2%E7%BC%96%E8%AF%91%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F.png)
    ```python
    import re
    
    p = r'\w+@zhijieketang\.com'
    regx = re.compile(p)

    text = "Tony's email is tony_guan588@zhijieketang.com."
    m = regex.search(text) 
    print(m) # 匹配

    m = regex.match(text)
    print(m) # 不匹配

    p = r'[Jj]ava'
    regex = re.compile(p)
    text = 'I like Java and java.'

    match_list = regex.findall(text)
    print(match_list) # 匹配

    match_iter = regex.finditer(text)
    for m in match_iter:
        print(m.group())
    
    p = r'\d+'
    regex = re.compile(p)
    text = 'AB12CD34EF'

    clist = regex.split(text)
    print(clist)

    repace_text = regex.sub(' ',text)
    print(repace_text)
    ```
2. 编译标志
    - ASCII和Unicode  
        ```python
        import re
        text = '你们好Hello'
        p = r'\w+'
        regex = re.compile(p,re.U)

        m = regex.search(text)
        print(m) # 匹配

        m = regex.math(text)
        print(m) # 匹配

        regex = re.compile(p,re.A)

        m = regex.search(text)
        print(m) # 匹配

        m = regex.match(text)
        print(m) # 不匹配
        ```
    - 忽略大小写re.I
        re.compile(p,re.I)：p为规则
        ![](./img/%E5%BF%BD%E7%95%A5%E5%A4%A7%E5%B0%8F%E5%86%99.png)
    - 点元字符匹配换行符  
        ![](./img/%E7%82%B9%E5%85%83%E5%AD%97%E7%AC%A6%E5%8C%B9%E9%85%8D%E7%AC%A6.png)
    - 多行模式
        ```python
        import re
        p = r'^World'
        regex = re.compile(p)

        m = regex.search('Hello\nWorld.')
        print(m) # 不匹配

        regex = re.compile(p,re.M)
        m = regex.search('Hello\nWorld.')
        print(m) # 匹配

        ```
    - 详细模式
        ![](./img/%E8%AF%A6%E7%BB%86%E6%A8%A1%E5%BC%8F.png)