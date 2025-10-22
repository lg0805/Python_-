num_one = int(input("请输入一个整数："))
num_two = int(input("请输入一个整数："))
num_three = int(input("请输入一个整数："))
if num_one > num_two:
    if num_one > num_three:
        print("最大的数是：", num_one)
    else:
        print("最大的数是：", num_three)
else:
    if num_two > num_three:
        print("最大的数是：", num_two)
    else:
        print("最大的数是：", num_three)
