def computing_ladder(n):
    print("在1-%d之间的阶梯数为："%n)
    sum=0
    for i in range(7,n+1):
        if (i%7==0)and(i%6==5)and(i%5==4)and(i%3==2):
            sum=sum+i
            print("%d"%i)
    print("在1-%d之间，有%d个数可以满足爱因斯坦对阶梯的要求。"%(n,sum))
if __name__=="__main__":
    flag=1
    while flag:
        n=int(input("请输入n值："))
        computing_ladder(n)
        flag=int(input("继续请按1，结束请按0"))