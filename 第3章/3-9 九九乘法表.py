for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + str("*") + str(i) + "=" + str(i * j), end="\t")
    print()  # 换行输出
