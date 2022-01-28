import urllib.request
import urllib.parse

url = 'http://www.51work6.com/service/mynotes/WebService.php'
params_dict = {'email':121@qq.com,'type':'JSON','action':'query'}
params_str = urllib.parse.urlencode(params_dict)
print(params_str)
# params_bytes = params_str.encode()#字符串转换为字节序列对象

url = url + '?' + params_str
print(url)

req = urllib.request.Request(url)
# 发送post请求
# req = urllib.request.Request(url,data=params_bytes)# 发送POST请求
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    print(json_data)