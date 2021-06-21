#导入需要的库
from math import fabs
from math import modf
from math import pi
import os

#弧度转换
def rad_trans(x):
    a = x * pi / 180
    return(a)

#计算n的阶乘
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

#tan函数定义
def arctan_(x):
    x = modf(x)[0]
    a = x
    for i in range(1,50):
        a = a + pow(-1,i) * pow(x,2*i+1) / (2*i+1)
    return(a)

#输出结果
a = float(input())
print('={:.7f}'.format(arctan_(a)))
os.system("pause")