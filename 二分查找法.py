if __name__=='__main__':
    a=[1,2,3,4,45,56,567,765,8887,9999,97865]
    low=0
    n=len(a)
    high=n-1
    k=-1
    print('a数组中的数据如下：')
    for i in a:
        print(i,end=' ')
    print()
    m=int(input('输入查询的数m=：'))
    while low<=high:
        mid=(low+high)//2
        if m<a[mid]:
            high=mid-1
        else:
            if m>a[mid]:
                low=mid+1
            else:
                k=mid
                break
    if k>=0:
        print("m=%d,序号=%d"%(m,k))
    else:#没找到k就不会被赋值，仍为一开始的负数
        print('没找到')
