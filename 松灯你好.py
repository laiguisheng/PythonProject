name = input("请输入你的姓名: ")
#用切片 [1:] 获取从第二个字开始到最后的所有字符
given_name = name[1:]
#使用 f-string (格式化字符串字面值) 来拼接并打印结果
#或者使用加号 + 来拼接字符串
print(f"{given_name}你好")