score=60
#if score<=60:#所有的符号一定要用英文!!!冒号不要忘了！
    #print("不及格")
    #pass#空语句表示结束
#if score>=60:
 #   print("及格")
 #  pass
#else:
 #   print("不及格")
 #   pass
#score=int(input('请输入您的成绩：'))#千万要检查语句缩进情况，开头顶格，后面对齐
#    print('A')
#    pass
#elif score>80:
#     print('B')
#    pass
#猜拳游戏
#0=石头，1=剪刀，2=布
#import random#随机数
#ount=1
#   person=int(input('请出拳：'))
#   computer=random.randint(0,2)
#    if person==0 and computer==1:
#       print('你赢了')
#       pass
#    elif person==1 and computer==2:
#       print('你赢了')
#        pass
#   elif person==2 and computer==0:
#        print('你赢了')
#      print('平手')
#       pass
#    else:
#        print('你输了')
#        pass
#count+=1





#if else 嵌套
#xuefen=int(input('请输入您的学分：'))
#if xuefen>=10:
#    score = int(input('请输入您的成绩：'))
#    if score>=80:
#        print('优秀')
#        pass
#    else:
#        print('一般')
#        pass
#    pass
#else:
#    print('不及格')
#输入1-50数据
#index=0
#while index<=49:
#    index+=1
#    print(index)
#    pass
#九九乘法表
#row=9#1
#while row>=1:#<=9
#    col=1
#    while col<=row:
#        print('%d*%d=%d ' %(row,col,row*col),end='')
#        col+=1
#        pass
#    row-=1#+=1
#    print()
#    pass
#直角三角形
#row=1
#while row<=7:
#    j=1
#    while j<=row:
#        print('*' ,end='')
#        j+=1
#        pass
#    print()
#    row+=1
#    pass
#等腰三角形
#row=1
#while row<=5:
#    j=1
#    while j<=5-row:
#        print(' ',end='')
#        j+=1
#        pass
#    k=1
#    while k<=2*row-1:
#        print('*',end='')
#        k+=1
#        pass
#    print()
#    row+=1
#    pass
#for循环
#tags='我爱学习'
#for item in tags:
#    print(item)
#    pass
sum=0
for data in range(1,101):#左边包含右边不包含
    sum+=data
    #print(data,end=' ')
    #pass
    #print("sum=%d"%sum)
from gapp import dgp
from numpy import exp
from scipy.special import gamma
X=[6.04,0.86,2.11,9.54,8.58]
Y=[2.29,0.39,-0.56,-3.12,-2.12]
Sigma=[0.28,0.36,0.22,0.19,0.23]
def invgamma(theta,a,b):
    s=theta[0]
    p=b**a/gamma(a)*s**(-1-a)*exp(-b/s)
    return p
g=dgp.DGaussianProcess(X,Y,Sigma,theta=[1,1],prior=invgamma,priorargs=(0.2,1),grad='False')












