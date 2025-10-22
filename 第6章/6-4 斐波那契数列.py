"""
使用递归解决 斐波那契数列

"""
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input('请输入一个正整数: '))
for i in range(1, num + 1):
    print(fibonacci(i), end=' ')


