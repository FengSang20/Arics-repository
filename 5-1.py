#第5讲 单元作业1
import numpy as np
ran=np.random.rand(1000)
num=int(input('输入1-100之间的整数：'))
print('序号\t索引值\t\t随机数')
m=0
#m：序号
for i in np.arange(1000):
    if i%num==0:
        m+=1
        print('%d\t%d\t%.16f' %(m,i,ran[i]))