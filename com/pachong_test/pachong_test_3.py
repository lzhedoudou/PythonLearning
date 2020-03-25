import re

content = 'Hello 1234567 World_This is a Regex Demo Hello 12342312367 World_This is a Regex Demo'
my_rst = re.compile('Hello\s(\d+)\sWorld.*Demo.*\s(\d+)')
rst = my_rst.findall(content)
print(rst)

#result = re.findall('Hello\s(\d+)\sWorld.*Demo', content)
#print(result)
##print(result.)#输出的是第一个()中正则表达式匹配到的字符串，即目标字符
##print(result.span())