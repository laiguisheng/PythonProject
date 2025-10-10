def selectionSort(a):
    #求出列表的长度
    n=len(a)

    for i in range(0,n-1):
        for j in range(i+1,n):
            #交换
            if a[j] < a[i]:
                t=a[i]
                a[i]=a[j]
                a[j]=t
    for i in a:
        print(i,end=' ')

if __name__=='__main__':
    print("请为列表元素赋值，列表末尾不能有空格：")
    x=input()
    a=x.split(" ")#以空格方式分割每个元素
    for i in range(0,len(a)):#输入多个值
        a[i]=int(a[i])
    print("你输入的列表元素为：\n",a)
    print('经过交换后的数组元素为：')
    selectionSort(a)