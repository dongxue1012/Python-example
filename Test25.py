#求1+2!+3!+...+20!的和。
Sum=0
factorial=1
num = int(input('请输入一个数字：'))
for i in range(1,num+1):
    factorial = factorial*i
    Sum +=factorial
print('阶乘之和：',Sum)

