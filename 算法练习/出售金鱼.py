#我写的代码
'''
if __name__=="__main__":
    epsilon=1e-9
    for x in range(23,1000,2):
        j=x
        for i in range(1,5):
            x=x-(x+1)//(i+1)
        x=x-11
        if abs(x) < epsilon:#abs()是绝对值函数
            print(j)
'''
#书上的代码
if __name__=="__main__":
    flag=0
    i=23
    while flag==0:
        j=1
        x=i
        while j<=4 and x>=11:
            if (x+1)%(j+1)==0:# 检查是否能整除
                x-=(x+1)//(j+1)# 使用整数除法
            else:
                x=0
                break# 一旦不能整除，立即跳出内层循环
            j=j+1
        if j==5 and x==11:# 检查是否完成了4次循环且结果为11
            print(i)
            flag=1
        i=i+2