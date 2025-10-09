if __name__=='__main__':
    cock=0
    while cock<=20:
        hen =0
        while hen<=33:
            chicken=100-hen-cock
            if 5*cock+3*hen+chicken/3.0==100:
                print('cock=%2d,hen=%2d,chicken=%2d\n' % (cock, hen, chicken))
            hen=hen+1
        cock=cock+1