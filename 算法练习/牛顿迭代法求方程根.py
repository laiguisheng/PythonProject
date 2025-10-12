def solution牛顿法(a, b, c, d):
    x=1.5
    x0=x#用所求得的x值代替x0原来的值
    #f用来描述方程的值，fd用来描述方程求导之后的值
    f=a*x0*x0*x0+b*x0*x0+c*x0+d
    fd=3*a*x0*x0+2*b*x0+c
    h=f/fd
    x=x0-h#求得更接近方程根的x值
    while abs(x-x0)>=1e-5:
        x0=x
        f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
        fd = 3 * a * x0 * x0 + 2 * b * x0 + c
        h = f / fd
        x = x0 - h#求得更接近方程根的x值
    return x

if __name__=='__main__':
    print('请输入方程的系数：')
    #a,b,c,d代表所求方程的系数
    a, b, c, d=map(float,input().split())
    print('方程的参数为',a,b,c,d)
    #x用来记录求得的方程根
    x=solution牛顿法(a, b, c, d)
    print('所求方程的根为x=%.6f'%x)