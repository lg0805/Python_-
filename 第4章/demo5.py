# 给定任意自然数n，对其所有小于n的正因数求和，如果恰好等于n则n称作完全数，如果大于n则称其为盈数，小于n则称其为亏数。
# 函数main)接收一个自然数n作为参数，要求判断n是完全数、盈数还是亏数，并返回判断结果。例如，
# main(6)返回'完全数
# main(19)返回亏数，

def main(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return '完全数'
    elif sum > n:
        return '盈数'
    else:
        return '亏数'

print(main(6))