#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
def bubbleSort(l):
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


l = [3, 5, 1]
a = bubbleSort(l)
print(a)
