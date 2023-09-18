import re
# 读取文件内容
with open("C:\\Users\\22476\Desktop\周杰伦.txt", "r", encoding='utf-8') as f:
    content = f.read()

# 删除不需要的字符
#content = content.replace("\n", "")  # 删除回车（换行符）

content = content.replace("\"", "")  # 删除引号
content = content.replace("{", "")  # 删除大括号（左）
content = content.replace("}", "")  # 删除大括号（右）
content = content.replace(" ", "")  # 删除大括号（右）
content = re.sub("[^\u4e00-\u9fa5，, 。？！“”‘’：；《》、]", "", content)
# content = content.replace(',', ',\n')

print(content[:100])
# 将处理后的内容写回文件
with open("周.txt", "w", encoding='utf-8') as f:
    f.write(content)



