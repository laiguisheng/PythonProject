"""
int(x)将其他类型转换成数字
ord(x)将字符转换成对应的Unicode码
str(x)将其他类型转换成字符串
chr(x)将十进制数字转换成对应的字符
"""
def char_to_num(ch):#将字符转换成数字
    if ch>='0' and ch<='9':
        return int(ch)#将数字字符转换成数字
    else:
        return ord(ch)#将字母字符转换成数字

def num_to_char(num):#将数字转换为字符
    if num>=0 and num<=9:
        return str(num)#将10以内的数字转换成字符串
    else:
        return chr(num)#将大于9的数字转换成字符

def source_to_decimal(temp,source):#source为原始进制的基数，temp为待转换的值
    decimal_num=0#存储展开之后的和
    for i in range(len(temp)):#累加
        decimal_num=(decimal_num*source)+char_to_num(temp[i])
    return decimal_num

def decimal_to_object(decimal_num,object):#十进制转换为其他进制，object为新数制的基数
    decimal=[]
    while decimal_num:
        decimal.append(num_to_char(decimal_num%object))#求出余数并转换为字符
        decimal_num=decimal_num//object#用十进制数除以基数
    return decimal

def output(decimal):#修改余数数制，如果不修改顺序相反
    f=len(decimal)-1
    while f>=0:
        print(decimal[f],end='')
        f-=1
    print()

if __name__ == '__main__':
    MAXCHAR=101#允许的最大字符串长度
    flag=1#存储是否退出程序的标志
    while flag:#1被python视为真，其实为flag=1
        #利用输入的flag值控制循环是否结束
        #将原数转换成十进制数
        #求出转换成目标数之后字符数组的长度
        #逆序打印字符数组
        print("转换前的数是：",end='')
        temp=input()
        print("转换前的数制是：", end='')
        source=int(input())
        print("转换后的数制是：", end='')
        object=int(input())
        print("转换后的数是：", end='')
        decimal_num=source_to_decimal(temp,source)
        decimal=decimal_to_object(decimal_num,object)
        output(decimal)
        print("继续请输入1，否则输入0")
        flag=int(input())
        #if(flag==0):
            #break
