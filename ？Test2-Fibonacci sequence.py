#输出1000以内的斐波那契数列
#斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

'''
a=0
b=1
while b < 1000:
    print(b)
    a, b = b, a+b
'''
#输出第10个斐波那契数列

def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a
# 输出了第10个斐波那契数列
print(fib(10))