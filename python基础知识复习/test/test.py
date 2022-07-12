import configparser

config = configparser.RawConfigParser() # 创建配置解析器对象

config.read('./Setup.ini',encoding='utf-8') # 读取并解析配置文件

print(config.sections()) # 返回所有节点

section1 = config['Startup'] # 返回Startup节点
print(config.options('Startup'))

print(config['Product']['msi'])

print(config['Windows 2000']['MajorVersion']) # 返回MajorVersion数据
print(config['Windows 2000']['ServicePackMajor'])

value = config.getint('Windows 2000','MajorVersion')
print(type(value))

value = config.getint('Windows 2000','MajorVersion')
print(type(value))