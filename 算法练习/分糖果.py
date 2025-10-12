def judge(candy):
    for i in range(10):
        if candy[0]!=candy[i]:
            return 1
    return 0
def printResult(s,j):
    print('%4d'%j,end="")
    k=0
    while k<10:
        print("%4d"%s[k],end="")
        k+=1
        j+=1
    print()
def giveSweets(sweet,j):
    t=[0]*10
    while judge(sweet)==1:
        for i in range(10):
            if sweet[i]%2==0:
                sweet[i]=sweet[i]//2
                t[i]=sweet[i]
            else:
                sweet[i]=(sweet[i]+1)//2
                t[i]=sweet[i]
        for n in range(9):
            sweet[n+1]=sweet[n+1]+t[n]
        sweet[0]=sweet[0]+t[9]
        j+=1
        printResult(sweet,j)
if __name__=='__main__':
    sweet=[10,2,8,22,16,4,10,6,14,20]
    print("child 1    2    3    4    5    6    7    8    9    10")
    print('......................................................')
    print("次数   糖果数")
    j=0
    print("%4d" % j,end="")
    for i in range(len(sweet)):
        print("%4d" % sweet[i],end="")
    print()
    giveSweets(sweet,j)