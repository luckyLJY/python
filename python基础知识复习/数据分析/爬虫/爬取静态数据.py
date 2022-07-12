import urllib.request

url = 'file:///C:/Users/ljy/Desktop/a.html'
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode('gbk')
    print(htmlstr)