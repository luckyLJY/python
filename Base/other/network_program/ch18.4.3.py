import urllib.request

with urllib.request.urlopen('http://www.sina.com.cn/') as response:
    data = response.read()
    html = data.decode()
    print(html)

