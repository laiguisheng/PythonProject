#if true 是一个固定语句，后面的代码总是被执行
if True:
    print("hello,world")
else:
    print("hell,world")
'''
这是
一段
注释
'''
print("注释结束")
# code: GB2312
#变量名只能使用字母或下划线开头，除了下划线不得包含任何其他符号，剩下的可以是字母或数字或下划线
import keyword
print(keyword.kwlist)
print(type(keyword.kwlist))
