"""
根据身高体重计算某个人的BMI指数:
体质指数（BMI）=体重（kg）÷身高^2（m）

"""
height = float(input('请输入您的身高(m):'))
weight = float(input('请输入您的体重(kg):'))
BMI = weight / (height * height)
print('您的BMI值为:',BMI)
