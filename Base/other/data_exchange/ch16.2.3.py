import xml.etree.ElementTree as ET

tree = ET.parse('data/Notes.xml')
root = tree.getroot()

node = root.find("./Note") # 当前节点的第一个Note子节点
print(node.tag,node.attrib)

node = root.find("./Note/CDate") # Note子节点下的第一个CD节点
print(node.text)

# Note几点
node = root.find("./Note/CDate/..")
print(node.tag,node.attrib)

# 当前节点查找所有后代节点中第一个CDate节点
node = root.find(".//CDate")
print(node.text)

# 具有id属性的Note节点
node = root.find("./Note[@id]")
print(node.tag,node.attrib)

# id属性等于‘2’的Note节点
node = root.find("./Note[@id='2']")
print(node.tag,node.attrib)

# 第二个Note节点
node= root.find("./Note[2]")
print(node.tag,node.attrib)

# 最后一个Note几点
node = root.find("./Note[last()]")
print(node.tag,node.attrib)

# 倒数第2个Note几点
node = root.find("./Note[last()-1]")
print(node.tag,node.attrib)
