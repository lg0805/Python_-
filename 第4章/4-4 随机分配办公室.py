import random

# 定义一个列表用来保存3个办公室
offices = [[], [], []]
# 定义一个列表用来存储8位老师的名字
names = ['张老师', '李老师', '赵老师', '高老师',
         '刘老师', '周老师', '王老师', '吴老师']
for name in names:
    # 将8位老师按照索引为0、1、2进行分组
    index = random.randint(0, 2)
    # print(index)
    # 将8位老师放在不同列表中
    offices[index].append(name)
flag = 1
for tempNames in offices:
    print('办公室%d的人数为：%d' % (flag, len(tempNames)))
    flag += 1
    for name in tempNames:
        print("%s" % name, end=' ')
    print(" ")