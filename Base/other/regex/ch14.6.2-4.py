import re

p = r'^World'
regex = re.compile(p)

m = regex.search('Hello\nWorld.')
print(m)    #不匹配

regex = re.compile(p,re.M)
m = regex.search('Hello\nWorld.')
print(m)    #匹配