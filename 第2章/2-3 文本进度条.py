import time

incomplete_sign = 50   # .的数量
print('='*23+'开始下载'+'='*25)
for i in range(incomplete_sign + 1):
    completed = "*" * i   # 表示已完成
    incomplete = "." * (incomplete_sign - i)  # 表示未完成
    percentage = (i / incomplete_sign) * 100  # 百分比
    print("\r{:.0f}%[{}{}]".format(percentage, completed, incomplete), end="")
    time.sleep(0.5)
print("\n" + '='*23+'下载完成'+'='*25)



"""
本案例涉及到print()函数、for循环、以及format()方法的使用。首先定义一个变量接收总的任务量，
然后在for循环体中编写表示已完成、未完成、完成百分比，最后使用format()方法将字符串进行格式化输出，
需要说明的是\r在这里表示将默认输出的内容返回到第一个指针，后面的内容会覆盖掉前面的内容，这样就达到了
实时显示进度条的功能。



\r 默认表示将输出的内容返回到第一个指针，这样的话，后面的内容会覆盖前面的内容
"""