raw_data = input('请输入密码：')
num_asc = 0   # ASCII累加值
str_pwd = ''  # ASCII拼接值
for i in raw_data:
    ascii_val = ord(i)              # 1.获取每个元素的ASCII值
    num_asc = ascii_val + num_asc   # 2.对遍历的ASCII值进行累加操作
    str_pwd += str(ascii_val)       # 3.拼接操作
    reversal_num = str_pwd[::-1]    # 4.将拼接的ASCII值倒序排列
    encryption_num = int(reversal_num) + num_asc  # 5.进行运算操作
print(f"加密后的密码为：{encryption_num}")