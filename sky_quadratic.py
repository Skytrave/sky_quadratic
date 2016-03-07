# -*- coding: utf:8 -*-
# 一元二次方程组
import math
def sky_quadratic(a,b,c):
    w=b*b-4*a*c
    if a==0 and b==0 and c!=0:
        pass
        print('error')
    elif a==0:
        x=-(c/b)
        return x
        print (x)
    elif w>=0:
        x1=(-b+math.sqrt(w))/(2*a)
        x2=(-b+math.sqrt(w))/(2*a)
        return ('%.2f,%.2f'%(x1,x2))
    else:
        pass
        print('error')
        
sky_1=ord(input('This is a magic,If you want to continue,please input "Y", if not please input "N" ',))      
while sky_1==89:
    a=float(input('please input a:'))
    b=float(input('please input b:'))
    c=float(input('please input c:'))
    print('The solution is:',sky_quadratic(a,b,c))
    sky_1=ord(input('If you want to continue,please input "Y", if not please input "N" ',))
    if sky_1==78:
        break

    
 