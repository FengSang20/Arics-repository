#第5讲 单元作业2
import numpy as np
x=np.array([65.3,99.6,145.64,63.75,135.46,92.85,85.48,98.97,144.76,116.03])
y=np.array([65.55,82.43,132.85,73.31,131.05,86.57,85.43,84.33,113.25,110.32])
x_=np.sum(x+y)/len(x)    #x_:数组x的均值
y_=np.sum(x+y)/len(y)    #y_:数组y的均值
Wu=Wd=0
for i in np.arange(len(x)):
    Wu+=(x[i]-x_)*(y[i]-y_)  #Wu：分子
    Wd+=(x[i]-x_)**2        #Wd:分母
W=Wu/Wd
b=y_-W*x_
print('W值为：%.2f,b的值为：%.2f' %(W,b))