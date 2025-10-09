if __name__=='__main__':
    tu1=1
    tu2=1
    i=3
    #输出第一个月和第二个月的兔子对数
    print("%6d        %6d" % (tu1,tu2),end="    ")
    while i<=100:
        tu=tu1+tu2#迭代求出当前月份的兔子对数
        print('%6d'%tu,end="    ")#输出当前月份的兔子对数
        if i%4==0:
            print()#每行输出4个
        tu2=tu1#为下一次迭代做准备，求出新的tu2
        tu1=tu#求出新的tu1
        i=i+1

