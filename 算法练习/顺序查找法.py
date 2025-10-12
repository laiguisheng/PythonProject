#我的代码
if __name__ == '__main__':
    a=[2,31,34,2,34213,432,2,1,65,8,54,21,85,4152,15,4,545,15,4,641,3865,87,5,4132,4165,486,7]
    print('a数组中的数据如下：')
    m=int(input('输入查询的数m=：'))
    for index, value in enumerate(a):
        if value == m:
            print(f"找到了！m={m}, 序号={index}")
            break
    else:
        # 这是 for 循环的 else 子句，而不是 if 的！
        # 它在 for 循环正常、完整地结束（即没有被 break 中断）时执行。
        print('没找到')
#书的代码
if __name__ == '__main__':
    a=[1,54,54,12,25,45,2,2,5,69,98,23,54,5,7,856,23,32,3548,523,15,45,456,78,4]
    k=-1
    print('a数组中的数据如下：')
    for i in a:
        print(i,end=' ')
    print()
    m=int(input('输入查询的数m=：'))
    i=0
    while i<len(a):
        if m==a[i]:
            k=i
            break
        i=i+1
    if k>=0:
        print("m=%d,序号=%d" % (m, k))
    else:  # 没找到k就不会被赋值，仍为一开始的负数
        print('没找到')