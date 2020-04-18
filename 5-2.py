#第5讲 单元作业2
import numpy as np
x=np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
x_=y_=0         #x_:求数组x的和，y_:数组y的和
for i in np.arange(len(x)):
    x_+=x[i]
    y_+=y[i]
x_=x_/len(x)
y_=y_/len(y)
Wu=Wd=0
for i in np.arange(len(x)):
    Wu+=(x[i]-x_)*(y[i]-y_)  #Wu：分子
    Wd+=(x[i]-x_)**2         #Wd:分母
W=Wu/Wd
b=y_-W*x_
print('W值为：%.2f,b的值为：%.2f' %(W,b))