# 梅森素数是指形如2^k-1的素数。数学家已经证明，如果2^k-1是素数，那么k必然也是素数
# 函数main()接收一个自然数num作为参数，要求返回大于num的最小梅森素数以及对应的k值组成的元组。例如，
# main(199)返回(7，127),
# main(1009)返回(13，8191)

# def main(num):
#     start = int(math.log2(num))
#     for k in range(start, 2 * start):
#         if is_prime(k):
#             if is_prime(2 ** k - 1):
#                 return k, 2 ** k - 1


# def main(num):
#     start = int(math.log2(num))
#     for k in range(start, 2 * start):
#         if is_prime(k):
#             if is_prime(2 ** k - 1):
#                 return k, 2 ** k - 1
#
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main(num):
    start = 0
    while 2 ** start - 1 <= num:
        start += 1

    for k in range(start, 2 * start):
        if is_prime(k):
            if is_prime(2 ** k - 1):
                return k, 2 ** k - 1


print(main(1009))
