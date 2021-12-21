import re
text = '你们好Hello'

p = r'\w+' #匹配数字字母下滑线
regex = re.compile(p,re.U)

m = regex.search(text)
print(m)    #匹配

m = regex.match(text)
print(m)   #匹配

regex = re.compile(p,re.A)

m = regex.search(text)
print(m)  #匹配

m = regex.match(text)
print(m) # 不匹配