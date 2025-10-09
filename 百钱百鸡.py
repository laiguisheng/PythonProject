if __name__=='__main__':
       #
       #
       cock=0
       while cock<=20:
              #
              hen=0
              while hen<=33:
              #
                     chicken=0
                     while chicken<=100:
                     #
                            if (5*cock+3*hen+chicken/3.0==100)and(cock+hen+chicken==100):
                                  print('cock=%2d,hen=%2d,chicken=%2d\n'%(cock,hen,chicken))
                            chicken=chicken+1
                     hen=hen+1
              cock=cock+1