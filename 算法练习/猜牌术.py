if __name__=="__main__":
    a=[0]*14
    j=1
    print("魔术师手中的牌的次序是：")
    for i in range(14):
        n=1
        while n<=i:
            if j>13:
                j=1
            if a[j]:
                j=j+1
            else:
                if n==i:
                    a[j]=i
                j=j+1
                n=n+1
    print(a[1:])