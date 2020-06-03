#用递归的方法求5！
def fac(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j *fac(j - 1)
    return sum
print(fac(5))