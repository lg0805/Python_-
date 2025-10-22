"""
根据用户输入的数据实现计算BMI值
"""
'''
体质指数（BMI）=体重（kg）÷身高*身高（m）
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
'''
# 将输入的身高体重转换为float类型
height = float(input('请输入您的身高(m):'))
weight = float(input('请输入您的体重(kg):'))
BMI = weight / (height * height)
print('您的BMI值为%.2f' % BMI)
if BMI < 18.5:
    print('体重过轻')
elif 18.5 <= BMI <= 23.9:
    print('体重正常')
elif 24 <= BMI <= 27:
    print('体重过重')
elif 28 <= BMI <= 32:
    print('体重肥胖')
else:
    print('非常肥胖')
