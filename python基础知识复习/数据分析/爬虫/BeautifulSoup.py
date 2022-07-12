import urllib.request
import os

from bs4 import BeautifulSoup

url ='http://p.weather.com.cn/'

def findallimageurl(htmlstr):
    """从HTML代码中查找匹配的字符串"""

    sp = BeautifulSoup(htmlstr,'html.parser')
    # 返回所有的img标签对象
    imgtaglist = sp.find_all('img')

    # 从img标签对象列表中返回对应的src列表
    srclist = list(map(lambda  u:u.get('src'),imgtaglist))

    # 过滤掉非.png和.jpg结尾文件src字符串
    filtered_srclist = filter(lambda u:u.lower().endswith('.png')or u.lower().endswith('.jpg',srclist))

    return filtered_srclist

def getfilename(urlstr):
    """根据图片链接地址获取图片名"""
    pos = urlstr.rfind('/')
    return urlstr[pos+1:]

# 分析获得url列表
url_list = []
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()

    url_list = findallimageurl(htmlstr)
for imagesrc in url_list:
    # 根据图片地址下载
    req = urllib.request.Request(imagesrc)
    with urllib.request.urlopen(req) as response:
        data = response.read()

        # 过滤掉小于100kb的图片
        if len(data) < 1024*1000:
            continue

        # 创建download文件夹
        if not os.path.exists('download'):
            os.mkdir('download')

        # 获得图片名
        filename = getfilename(imagesrc)
        filename = 'download/'+filename

        # 保存图片到本地
        with open(filename,'wb') as f:
            f.write(data)

    print('下载图片',filename)





















