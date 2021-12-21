import re
p = r'(java).*(python)'
regex = re.compile(p,re.I)

m = regex.search('I like Java and Python.')
print(m)    #匹配

m = regex.search('I like JAVA and Python.')
print(m)    #匹配

rn = regex. search('I like java and Python.')
print(rn) #匹配