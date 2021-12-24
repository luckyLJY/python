import configparser

# 创建配置解析器对象
config = configparser.ConfigParser()
# 读取并解析配置文件
config.read('data/Setup.ini',encoding='utf-8')
# 返回所有的节点
print("返回所有的节点{0}".format(config.sections()))

# 返回Starup节点
section1 = config['Startup']
print("Startup节点：{0}".format(config.options('Startup')))

print("RequireOS节点{0}".format(section1['RequireOS']))
print("RequireIE节点{0}".format(section1['RequireIE']))

print("Product-mis节点{0}".format(config['Product']['msi']))

# 返回MajorVersioin数据
print(config['Windows 2000']['MajorVersion'])
print(config['Windows 2000']['ServicePackMajor'])

# 返回MajorVersion数据--得到的类型为string
value = config.get('Windows 2000','MajorVersion')
print("get数据返回类型：{0}".format(type(value)))

# 返回MajorVersion数据--得到的类型为int
value = config.getint('Windows 2000','MajorVersion')
print("getint数据返回类型:{0}".format(type(value)))