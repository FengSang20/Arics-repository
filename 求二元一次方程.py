#求二元一次方程:ax^2+bx+c=0并判断是否有解，有则输出x。
import math
a=int(input('请输入a:'))
b=int(input('请输入b:'))
c=int(input('请输入c:'))
print('你输入的a,b,c分别为：{} {} {}'.format(a,b,c))
k=b**2-4*a*c
if a==0:
    print('请重新输入a的值')
a=int(input('请输入a:'))
if k>0:
    x1=(-b+math.sqrt(k))/(2*a)
    x2=(-b-math.sqrt(k))/(2*a)
    print("x的值分别为:{:.2f}、{:.2f}".format(x1,x2))
if k==0:
    x=(-b)/(2*a)
    print('x的值为：{:.2f}'.format(x))
if k<0: 
    print('方程无解')
