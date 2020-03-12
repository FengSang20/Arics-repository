#第6讲 单元作业2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

boston_housing=tf.keras.datasets.boston_housing
(train_x,train_y),(_,_)=boston_housing.load_data(test_split=0)
plt.figure(figsize=(12,20))
titles=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT']
for i in np.arange(13):
    plt.subplot(4,4,i+1)
    plt.scatter(train_x[:,i],train_y)
    plt.title(str(i+1)+'.'+titles[i]+'-Price')
    plt.xlabel(titles[i])
    plt.ylabel("Price(-$1000's)")
    plt.ylim(0,60)
plt.suptitle('各个属性与房价的关系',fontsize=14)
plt.rcParams["font.sans-serif"]="SimHei"
plt.tight_layout(rect=[0,0,1,0.9])
plt.show()
for j in np.arange(13):
    print(str(j+1)+'--'+titles[j])
inp=int(input('请选择属性：'))
for m in np.arange(1,14):
    if inp==m:
        plt.scatter(train_x[:,m-1],train_y)
        plt.title(str(m)+'.'+titles[m-1]+'-Price')
        plt.xlabel(titles[m-1])
        plt.ylabel("Price(-$1000's)")
        plt.ylim(0,60)
plt.show()

