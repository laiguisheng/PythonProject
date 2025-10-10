def runYear(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return 1
    else:
        return 0

def countDay(currentDay):
    permonth=[0,31,28,31,30,31,30,31,31,30,31,30]
    totalDay=0
    year=1990
    while year<currentDay['year']:
        if runYear(year)==1:
            totalDay += 366
        else:
            totalDay += 365
        year+=1
    if runYear(currentDay['year'])==1:
        permonth[2]+=1
    i=0
    while i<currentDay['month']:
        totalDay += permonth[i]
        i+=1
        totalDay += currentDay['day']
        return totalDay

if __name__=="__main__":
    while(True):
        print("输入年月日，如1999 1 31")
        year,month,day=[int(i) for i in input().split()]
        #定义一个日期字典
        today={'year':year,'month':month,'day':day}
        totalDay=countDay(today)
        print("%d年%d月%d日与1990年1月1日相差%d天"%(year,month,day,totalDay))
        result = totalDay%5
        if result>0 and result<4:
            print("今天约跑")
        else:
            print("今天打胶")
