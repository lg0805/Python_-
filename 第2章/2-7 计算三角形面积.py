one_len = float(input('输入三角形第一边长: '))
two_len = float(input('输入三角形第二边长: '))
three_len = float(input('输入三角形第三边长: '))
# 计算半周长
s = (one_len + two_len + three_len) / 2
# 计算面积
area = (s * (s - one_len) * (s - two_len) * (s - three_len)) ** 0.5
print('三角形面积为%0.1f' % area)
