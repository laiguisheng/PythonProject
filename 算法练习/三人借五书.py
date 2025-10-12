if __name__=='__main__':
    i=0
    print("A,B,C三人所选书号分别为：")
    for a in range(1,6):
        for b in range(1,6):
            for c in range(1,6):
                if a!=b and a!=c and b!=c:
                    print("A:%2d B:%2d C:%2d   "%(a,b,c),end='')
                    i=i+1
                    if i%4==0:
                        print()
    print("共有%d种有效借阅方法"%i)