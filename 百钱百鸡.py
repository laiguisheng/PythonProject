if __name__=='__main__':
       #cock表示公鸡，hen表示母鸡，chicken表示小鸡，总共100只
       #外层循环控制公鸡数量取值范围为0~33
       cock=0
       while cock<=20:
              #内层循环控制母鸡数量
              hen=0
              while hen<=33:
              #内层循环控制小鸡数量
                     chicken=0
                     while chicken<=100:
                     #条件控制
                            if (5*cock+3*hen+chicken/3.0==100)and(cock+hen+chicken==100):
                                  print('cock=%2d,hen=%2d,chicken=%2d\n'%(cock,hen,chicken))
                            chicken=chicken+1
                     hen=hen+1
              cock=cock+1