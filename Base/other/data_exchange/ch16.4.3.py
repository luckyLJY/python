import configparser

# 创建配置解析器对象
config = configparser.ConfigParser()

# 读取配文件
config.read('data/Setup.ini',encoding='utf-8')

# 写入配置文件
config['Startup']['RequireMSI'] = '8.0'
config['Product']['RequireMSI'] = '4.0'

# 添加节点
config.add_section('Section2')
# 添加配置项
config.set('Section2','name','Mac')

with open('data/Setup.ini','w') as fw:
    config.write(fw)