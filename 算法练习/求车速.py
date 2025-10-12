if __name__=="__main__":
    flag=1
    i=95860
    while(flag==1):
        i=i+1
        a=list(str(i))
        b=[int(c)for c in a]
        if (a[0]==a[4])and(a[1]==a[3]):
            flag=0
            j=i
    print(i)
    print((i-95859)//2)