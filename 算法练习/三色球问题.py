if __name__ == '__main__':
    print("\t 红球 \t 白球 \t 黑球")
    print("......................")
    num=0
    for m in range(0,4):
        for n in range(0,4):
            if 8-m<=6:
                num=num+1
                print('%2d: %d \t\t %d \t\t %d'%(num,m,n,8-m-n))