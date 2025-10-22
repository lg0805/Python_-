"""
好友系统
增加
删除
修改
查询

"""

# 好友管理系统

# 定义一个空的好友列表
friends = []

# 打印欢迎信息和功能选项
print("欢迎使用好友系统")
print("1：添加好友")
print("2：删除好友")
print("3：备注好友")
print("4：展示好友")
print("5：退出")

# 循环接收用户输入的选项
while True:
    num = int(input("请输入您的选项："))

    # 添加好友
    if num == 1:
        add_friend = input("请输入要添加的好友：")
        friends.append(add_friend)  # 添加好友
        print('好友添加成功')

    # 删除好友
    elif num == 2:
        del_friend = input("请输入删除好友姓名：")
        friends.remove(del_friend)      # 删除好友
        print("删除成功")

    # 备注好友
    elif num == 3:
        before_friend = input("请输入要修改的好友姓名：")
        after_friend = input("请输入修改后的好友姓名：")
        friend_index = friends.index(before_friend) # 获取要修改的好友的索引
        friends[friend_index] = after_friend    # 修改好友姓名
        print("备注成功")

    # 展示好友列表
    elif num == 4:
        if len(friends) == 0:
            print("好友列表为空")
        else:
            for i in friends:
                print(i)

    # 退出程序
    elif num == 5:
        break
