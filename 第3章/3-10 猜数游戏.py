import random
print("猜数字游戏,输入一个1-100以内的数字")
random_num = random.randint(1, 100)
# print(random_num)  # 打开注释可查看生成的随机数
for frequency in range(1,6):
    number = input("请输入一个数字:")
    if number.isdigit() is False:
        print('请输入一个正确的数字')
    elif int(number) < 0 or int(number) > 100:
        print("请输入1-100范围的数字")
    elif random_num == int(number):
        print("恭喜你用了%d次猜对了" % frequency)
        break
    elif random_num > int(number):
        print("很遗憾，你猜小了")
    else:
        print("很遗憾，你猜大了")
    if frequency == 5:
        print("很遗憾，%d次机会已用尽，游戏结束,答案为%d" %
              (frequency, random_num))


# import random
# name = input('您的大名是？')
# print('您好，' + name + '！我们来玩儿猜数字游戏吧！')
# minNum = int(input('请输入一个最小值：'))
# maxNum = int(input('再输入一个最大值：'))
# secret = random.randint(minNum, maxNum)
# guess = 0
# tries = 0
# while guess != secret and tries < 5:
#     guess = int(input('猜数字游戏开始，请输入数字：'))
#     if guess > secret:
#         print('您输入的数字大了！')
#     elif guess < secret:
#         print('您输入的数字小了！')
#     tries += 1
#     print('这是您第' + str(tries) + '次尝试！')
# if guess == secret:
#     print('恭喜，您猜对了！')
#     print('游戏结束，再见！^_^')
# else:
#     print('哦哟，机会用完了，下次再来吧！')
