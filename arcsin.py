#导入需要的库
from math import fabs
from math import pi
from math import modf
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

#双阶层函数
def doublefactorial(n):
     if n <= 0:
        return 1
     else:
        return n * doublefactorial(n-2)

#arcsin函数定义
def arcsin_(x):
    x = modf(x)[0]
    a = x
    for i in range(1,50):
        a = a + (pow(x,2*i+1) * doublefactorial(2*i-1)) / ((2*i+1) * doublefactorial(2*i))
    return(a)

#输出结果
a = float(input())
print('={:.7f}'.format(arcsin_(a)))
os.system("pause")