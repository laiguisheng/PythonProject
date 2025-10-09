if __name__=="__main__":
    #i代表前两位车牌号的数字，j代表后两位车牌号的数字，k代表车牌号
    flog=0               #循环标识变量，为1时退出所有循环
    for i in range(10):
        if flog:
            break
        for j in range(10):#穷举前两位和后两位车牌数字
            if flog:
                break
                #判断前两位和后两位数字是否相同
            if i!=j:
                #组成4位车牌号码
                k=1100*i+11*j
                #判断k是否是某个数的平方，是就输出
                for temp in range(31,100):
                    if temp**2 == k:
                        print("车牌号为",k)
                        flog=1
                        break