num3 = int(input("请输入一个三位数："))
hundreds_place = int(num3 // 100 % 10)  # 百位
ten_place = int(num3 / 10 % 10)  # 十位
one_place = int(num3 % 10)  # 个位
if hundreds_place ** 3 + ten_place ** 3 + one_place ** 3 == num3:
    print(f"{num3}是水仙花数")
else:
    print(f"{num3}不是水仙花数")