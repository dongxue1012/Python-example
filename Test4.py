#输出200以内所有素数
#一个数变为两个数的积，将范围缩小，在一般领域，对正整数n，如果用2到sqrt（）之间的所有整数去除，均无法整除，则n为质数。
import math
num = 0

for i in range(2,100):
    m = int(math.sqrt(i))
    k= True
    for j in range(2,m+1):
        if (i%j == 0):
            k = False
            break
    if (k == True):
        print(("%d"%i))
        num = num+1
print("素数个数%d"%num)